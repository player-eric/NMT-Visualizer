import http.server
import socketserver
import webbrowser

def call_html():
    PORT = 8888
    Handler = http.server.SimpleHTTPRequestHandler
    while(True):
        try:
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("web page serving at port http://localhost:", PORT)
                webbrowser.open('http://localhost:'+str(PORT)+'/')
                httpd.serve_forever()
        except:
            PORT+=1
        

