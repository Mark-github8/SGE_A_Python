from coche import Coche
from colibri import Colibri

#instancia objeto Coche
Coche_1 = Coche(marca="volwagen",motor="electrico", color="verde", peso="2 toneladas", kilometros="1423K")
Coche_2 = Coche(marca="nisan",motor="hibrido", color="rojo", peso="1.4 toneladas", kilometros="1048K")
Coche_3 = Coche(marca="Honda",motor="diesel", color="mate", peso="3 toneladas", kilometros="3029K")
print(f'La marca de mi coche es {Coche_1.getMarca()}')
print(f'M coche es de color {Coche_1.getColor()}')
print(f'M coche tiene un motor {Coche_1.getMotor()}')

#instancia objeto Colibri
Colibri_1 = Colibri(especie = "volatus", dieta = "semillas", color = "verde", velocidad = "20k/h", peso = '1000gr')
Colibri_2 = Colibri(especie = "birbtus", dieta = "frutas", color = "amarillo", velocidad = "30k/h", peso = '800gr')
Colibri_3 = Colibri(especie = "speedyboy", dieta = "mixto", color = "negro", velocidad = "40k/h", peso = '600gr')
print(f'Mi colibrí tiene una dieta de {Colibri_1.getDieta()}')
print(f'Mi colibrí es de color {Colibri_2.getColor()}')
print(f'Mi colibrí pesa {Colibri_1.getPeso()}')

#Modificar 2 atributos de coche a traves de los setters
Coche_1.setColor("rosa")
Coche_1.setKilometros("2400K")

#Mostrar los 2 atributos modificados a través de los getters
print("\nAtributos modificados del coche 1:")
print(f"Marca: {Coche_1.getMarca()}")
print(f"Motor: {Coche_1.getMotor()}")

#Modificar 2 atributos de colibrí a traves de los setters
Colibri_1.setEspecie("Slowpoke")
Colibri_1.setColor("blanco")

# Mostrar los atributos modificados a través de los getters
print("\nAtributos modificados del Colibrí 1:")
print(f"Color: {Coche_1.getColor()}")
print(f"Peso: {Coche_1.getPeso()}")
