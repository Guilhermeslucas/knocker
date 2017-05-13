import argparse
import socket
import time


def knock(host, knock_seq, delay):
    """Knock host and port using tcp connection"""

    for port in knock_seq:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)

        try:
            sock.connect((host, port))
        except socket.error:
            # Nothing really there...
            pass

        time.sleep(delay)


def main():
    parser = argparse.ArgumentParser(prog='knocker', description=knock.__doc__)
    parser.add_argument('host', help='Hostname or IP address of the host')
    parser.add_argument('ports', nargs='+', type=int, help='Ports to knock')
    parser.add_argument('-d', '--delay', type=int, default=200,
                        help='Milliseconds between each knock')

    args = parser.parse_args()

    print('knock... knock...')
    knock(args.host, args.ports, args.delay/1000)
