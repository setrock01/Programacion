import random
from typeguard import typechecked

class dado_finalV2:

    @typechecked
    def __init__(self, cara_superior=0, caras=6):
        self.cara_superior = cara_superior
        self.caras = caras

    @property
    def cara_superior(self):