  
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '$metadata':
            try:
                file_to_open = "data"
                self.send_response(200)
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))


PORT = 8080
httpd = HTTPServer(('localhost', PORT), Serv)
print("serving at port", PORT)
httpd.serve_forever()
