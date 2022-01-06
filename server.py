from http.server import BaseHTTPRequestHandler,HTTPServer
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
      GPIO.output(18, GPIO.HIGH)
      self.send_response(200)
      self.send_header('Content-type','text/xml')
      self.end_headers()
      self.wfile.write(bytes("on","utf"))
      self.wfile.flush()
    elif request == 'off':
      GPIO.output(18, GPIO.LOW)
      self.send_response(200)
      self.send_header('Content-type','text/xml')
      self.end_headers()
      self.wfile.write(bytes("off","utf"))
      self.wfile.flush()
    elif request == 'state':
      state=" "
      if GPIO.input(17):
        state = "Line tampered"
      elif not GPIO.input(27):
        state = "LOW POWER"
      elif not GPIO.input(22):
        state = "HIGH POWER"
      self.send_response(200)
      self.send_header('Content-type','text/xml')
      self.end_headers()
      self.wfile.write(bytes(state,"utf"))
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