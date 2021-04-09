import http.server
import socketserver


class myHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'myotherpage.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)


PORT = 8000

handler = myHandler

myServer = socketserver.TCPServer(("", PORT), handler)
myServer.serve_forever()