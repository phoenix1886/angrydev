from autocomplete_engine import AutocompleteEngine, parse_words_frequencies
import argparse
import socketserver
import re


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):

        client_request = str(self.request.recv(1024), 'utf-8')
        if re.match(r'GET\s+\S+', client_request):
            prefix = client_request.split()[1]
            possible_words = autocomplete_engine.autocomplete(prefix)
            response = bytes('\n'.join(possible_words), 'utf-8')
        else:
            response = bytes('Error 400. \nBad request.', 'utf-8')
        self.request.sendall(response)


class ThreadedEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='File path to dictionary')
    parser.add_argument('port', help='Port available for sever', type=int)

    arguments = parser.parse_args()
    return arguments


def start_server(adress):
    server = ThreadedEchoServer(adress, ThreadedTCPRequestHandler)
    print('starting server...')
    print('waiting for requests...')
    server.serve_forever()


if __name__ == '__main__':
    arguments = parse_args()
    port = arguments.port
    file_path = arguments.file_path

    with open(file_path) as file:
        words_frequencies = parse_words_frequencies(file)

    autocomplete_engine = AutocompleteEngine(
        words_frequencies
    )

    adress = ('', port)
    start_server(adress)
