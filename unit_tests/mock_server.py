"""Mock server"""
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockSWGOHGGServer(BaseHTTPRequestHandler):
    """Mocks the swgoh.gg website"""

    def do_GET(self):
        """responds to get requests to the server"""

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        file_path = 'data\{}'.format(self.path.replace('/', ''))

        with open(file_path, 'rb') as file:
            self.wfile.write(file.read())

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-port', metavar='port', help='port to use for the mock server', type=int)
    args = parser.parse_args()

    server_address = ('127.0.0.1', args.port)
    httpd = HTTPServer(server_address, MockSWGOHGGServer)
    httpd.serve_forever()
