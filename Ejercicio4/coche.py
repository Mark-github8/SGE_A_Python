class Coche:
    #constructor
    def __init__(self, marca, motor, color, kilometros, peso):
        #atributos
        self.marca = marca
        self.motor = motor
        self.color = color
        self.kilometros = kilometros
        self.peso = peso
    #getters y setters 
    def getMarca(self): 
        return self.marca
    def setMarca(self, new_marca): 
        self.marca = new_marca
        
    def getMotor(self): 
        return self.motor
    def setMotor(self, new_motor): 
        self.motor = new_motor

    def getColor(self): 
        return self.color
    def setColor(self, new_color): 
        self.color = new_color

    def getKilometros(self): 
        return self.kilometros
    def setKilometros(self, new_kilometros): 
        self.kilometro = new_kilometros

    def getPeso(self): 
        return self.peso
    def setPeso(self, new_peso): 
        self.kilometro = new_peso