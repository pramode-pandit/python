import http.server
import socketserver

class RequestHandler(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
       print (self.path)
       self.send_response(301)
       new_path = '%s%s'%('https://gist.github.com/shreddd/b7991ab491384e3c3331', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

socketserver.TCPServer(("", 8080), RequestHandler).serve_forever()