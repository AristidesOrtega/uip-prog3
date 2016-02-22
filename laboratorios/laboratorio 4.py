class Perro:
    def __init__(self, vida, alegria):
        self.vida= 5
        self.alegria= 5
    def caminar (self):
        self.vida=self.vida -2
        self.alegria=self.alegria +1
    def correr (self):
        self.vida=self.vida -4
        self.alegria=self.alegria +3
    def dormir (self):
        self.vida=self.vida +1
        self.alegria=self.alegria -3
    def jugar (self):
        self.vida=self.vida -3
        self.alegria=self.alegria +4
    def comer (self):
        self.vida=self.vida +5
        self.alegria=self.alegria +1

Lassie = Perro
