from http.server import BaseHTTPRequestHandler,HTTPServer

class myHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    if request == 'reading':
      self.path="log.xml"
      f = open(self.path)
      self.send_response(200)
      self.send_header('Content-type','text/xml')
      self.end_headers()
      self.wfile.write(bytes(f.read(),"utf"))
      f.close()
      self.wfile.flush()
    elif request == 'on':
      left=0
      self.send_response(200)
      self.send_header('Content-type','text/xml')
      self.end_headers()
      self.wfile.write(bytes("on","utf"))
      self.wfile.flush()
    elif request == 'off':
      left=1
      self.send_response(200)
      self.send_header('Content-type','text/xml')
      self.end_headers()
      self.wfile.write(bytes("off","utf"))
      self.wfile.flush()
    else:
      self.path="index.html"
      f = open(self.path)
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      self.wfile.write(bytes(f.read(),"utf"))
      f.close()
      self.wfile.flush()
    return

server = HTTPServer(("",8080), myHandler)
print ('Started httpserver on port 8080')
server.serve_forever()