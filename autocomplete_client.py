import socket
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='Host or IP adress of host')
    parser.add_argument('port', help='Port of host to connect', type=int)

    arguments = parser.parse_args()
    return arguments


def get_autocomplete_words(prefix, adress):
    request = 'GET {}'.format(prefix)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(adress)
        sock.sendall(bytes(request, 'utf-8'))

        response = b''
        tmp = sock.recv(1024)
        while tmp:
            response += tmp
            tmp = sock.recv(1024)
    return str(response, 'utf-8')


if __name__ == '__main__':
    arguments = parse_args()
    port = arguments.port
    host = arguments.host

    adress = (host, port)

    while True:
        prefix = input('Prefix: ')
        response = get_autocomplete_words(prefix, adress)
        print(response)


