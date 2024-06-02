import cherrypy

class HelloWorld:
    def index(self):
        return "Hello World!"
    index.exposed = True

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), '/', config={
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080,
        }
    })