from collections import namedtuple


# We'll use exceptions to notify the connection-handling loop of problems.
class CommandError(Exception): pass
class Disconnect(Exception): pass


Error = namedtuple('Error', ('message',))