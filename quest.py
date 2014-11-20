import json
import time
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		f = open("quests.json")
		allQuests = json.loads(f.read())

		currTime = time.time()
		availQuests = []
		for q in list(allQuests):
			if q['endTime'] > currTime:
				availQuests.append(q)

		str = json.dumps(availQuests, indent=4)
		print(str)
		self.wfile.write(str)
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
