#clase aleatorio
import random
class aleat():

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):

        aleatorio = random.randint(111111111, 999999999)

        url_aleatoria = "http://localhost:1234/aleat/" + str(aleatorio)

        return ("200 OK", "<a href=" + url_aleatoria + ">Dame otra</a>")
