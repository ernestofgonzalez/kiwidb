from kiwidb.server import Server


def main():
    from gevent import monkey; monkey.patch_all()
    server = Server()

    try:
        server.run()
    except KeyboardInterrupt:
        print('\x1b[1;31mshutting down\x1b[0m')


if __name__ == '__main__':
    main()