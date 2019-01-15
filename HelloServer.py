# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # note that the three parts of an HTTP response are: response code, headers, response body

        # send HTTP response
        self.send_response(200)

        # send HTTP Headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # send a message to the client via response body, in write only mode(wfile)
        # wfile is a variable in BaseHTTPREquestHandler class and stands for writeable file
        # self.wfile represents the connection from server to the client; and it is write-only.
        # write() is used to send response as response body
        self.wfile.write("Hello, from the HTTP Server!\n".encode())


if __name__ == '__main__':
    port_no = 8000
    server_address = ('', port_no) # serve all the addresses, on port 8000
    http_server = HTTPServer(server_address, HelloHandler)
    http_server.serve_forever()

