from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import json
import os

data = {'result': '你好'}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

def file_server(host="", port=11451, path="C:\\"):
    os.chdir(path)
    server = HTTPServer((host, port), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    file_server(path="E:\\")
