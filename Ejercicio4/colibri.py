class Colibri:
    #constructor
    def __init__(self, especie, dieta, color, velocidad, peso):
        #atributos
        self.especie = especie
        self.dieta = dieta
        self.color = color
        self.velocidad = velocidad
        self.peso = peso
    #getters y setters 
    def getEspecie(self): 
        return self.especie
    def setEspecie(self, new_especie): 
        self.especie = new_especie
        
    def getDieta(self): 
        return self.dieta
    def setDieta(self, new_dieta): 
        self.dieta = new_dieta

    def getColor(self): 
        return self.color
    def setColor(self, new_color): 
        self.color = new_color

    def getVelocidad(self): 
        return self.velocidad
    def setVelocidad(self, new_velocidad): 
        self.velocidad = new_velocidad

    def getPeso(self): 
        return self.peso
    def setPeso(self, new_peso): 
        self.peso = new_peso        