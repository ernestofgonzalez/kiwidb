import datetime
import sys
from collections import deque
from io import BytesIO

from kiwidb.error import CommandError, Disconnect, Error


if sys.version_info[0] == 3:
    unicode = str
    basestring = (bytes, str)


def encode(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    elif isinstance(s, bytes):
        return s
    else:
        return str(s).encode('utf-8')


def decode(s):
    if isinstance(s, unicode):
        return s
    elif isinstance(s, bytes):
        return s.decode('utf-8')
    else:
        return str(s)


class ProtocolHandler(object):
    def __init__(self):
        self.handlers = {
            '+': self.handle_simple_string,
            '-': self.handle_error,
            ':': self.handle_integer,
            '$': self.handle_string,
            '*': self.handle_array,
            '%': self.handle_dict}

    def handle_request(self, socket_file):
        first_byte = socket_file.read(1)
        if not first_byte:
            raise Disconnect()

        try:
            # Delegate to the appropriate handler based on the first byte.
            return self.handlers[decode(first_byte)](socket_file)
        except KeyError:
            raise CommandError('bad request')

    def handle_simple_string(self, socket_file):
        return socket_file.readline().rstrip(b'\r\n')

    def handle_error(self, socket_file):
        return Error(socket_file.readline().rstrip(b'\r\n'))

    def handle_integer(self, socket_file):
        return int(socket_file.readline().rstrip(b'\r\n'))

    def handle_string(self, socket_file):
        # First read the length ($<length>\r\n).
        length = int(socket_file.readline().rstrip(b'\r\n'))
        if length == -1:
            return None  # Special-case for NULLs.
        length += 2  # Include the trailing \r\n in count.
        return socket_file.read(length)[:-2]

    def handle_array(self, socket_file):
        num_elements = int(socket_file.readline().rstrip(b'\r\n'))
        return [self.handle_request(socket_file) for _ in range(num_elements)]

    def handle_dict(self, socket_file):
        num_items = int(socket_file.readline().rstrip(b'\r\n'))
        elements = [self.handle_request(socket_file)
                    for _ in range(num_items * 2)]
        return dict(zip(elements[::2], elements[1::2]))
    
    def write_response(self, socket_file, data):
        buf = BytesIO()
        self._write(buf, encode(data))
        buf.seek(0)
        socket_file.write(buf.getvalue())
        socket_file.flush()

    def _write(self, buf, data):
        if isinstance(data, bytes):
            buf.write(b'$%d\r\n%s\r\n' % (len(data), data))
        elif isinstance(data, unicode):
            bdata = data.encode('utf-8')
            buf.write(b'^%d\r\n%s\r\n' % (len(bdata), bdata))
        elif data is True or data is False:
            buf.write(b':%d\r\n' % (1 if data else 0))
        elif isinstance(data, (int, float)):
            buf.write(b':%d\r\n' % data)
        elif isinstance(data, Error):
            buf.write(b'-%s\r\n' % encode(data.message))
        elif isinstance(data, (list, tuple, deque)):
            buf.write(b'*%d\r\n' % len(data))
            for item in data:
                self._write(buf, item)
        elif isinstance(data, dict):
            buf.write(b'%%%d\r\n' % len(data))
            for key in data:
                self._write(buf, key)
                self._write(buf, data[key])
        elif isinstance(data, set):
            buf.write(b'&%d\r\n' % len(data))
            for item in data:
                self._write(buf, item)
        elif data is None:
            buf.write(b'$-1\r\n')
        elif isinstance(data, datetime.datetime):
            self._write(buf, str(data))