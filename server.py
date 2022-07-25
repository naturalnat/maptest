import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler #handles requests to server 
with socketserver.TCPServer(("", PORT), handler) as httpd:
  print("Server started at localhost:" + str(PORT))
  httpd.serve_forever() #runs server until killed 
