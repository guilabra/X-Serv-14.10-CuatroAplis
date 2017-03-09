#!/usr/bin/python3

"""
Ejercicio 14.10-CuatroAplis
Guillermo Labrador Vázquez
"""

import socket
import hola
import aleat
import suma

class app:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>" +
                          "Dumb application just saying 'It works!'" +
                          "</h1><p>App id: " + str(self) + "<p></body></html>")

class webApp:

    def select(self, request):

        resource = request.split(' ', 2)[1]
        for prefix in self.apps.keys():
            if resource.startswith(prefix):
                print("Running app for prefix: " + prefix + \
                    ", rest of resource: " + resource[len(prefix):] + ".")
                return (self.apps[prefix], resource[len(prefix):])
        print("Running default app")
        return (self.myApp, resource)

    def __init__(self, hostname, port, apps):

        self.apps = apps
        self.myApp = app()

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048).decode('utf-8')
            print(request)
            (theApp, rest) = self.select(request)
            parsedRequest = theApp.parse(request, rest)
            (returnCode, htmlAnswer) = theApp.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

if __name__ == "__main__":
    anApp = app()
    otherApp = app()
    holaApp = hola.hola()
    adiosApp = hola.adios()
    aleatApp = aleat.aleat()
    sumaApp = suma.suma()
    testWebApp = webApp("localhost", 1234, {'/app': anApp,
                                            '/other': otherApp,
                                            '/hola': holaApp,
                                            '/adios': adiosApp,
                                            '/aleat': aleatApp,
                                            '/suma': sumaApp})
