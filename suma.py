#clase suma
class suma():
    i = None

    def parse(self, request, rest):
        try:
            rest = int(rest[1:])
            return rest
        except ValueError:
            return None

    def process(self, parsedRequest):

        if (parsedRequest is None):
            return("200 OK", "<html><body><h1>" +
                              "No se han introducido datos" +
                              "</h1></body></html>")
        if(self.i is None):
            self.i = parsedRequest
            htmlAnswer = "<html><body> Me das un: " + str(parsedRequest) + "</body></html>"

        else:
            htmlAnswer = "<html><body> Me diste un: " + str(self.i) + ". Ahora me das un: " + str(parsedRequest) + ". Suman: " + str(parsedRequest + self.i) + "</body></html>"
            self.i = None

        return("200 OK", htmlAnswer)
