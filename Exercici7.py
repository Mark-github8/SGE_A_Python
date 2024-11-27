#RECOJER NUMERO
num = int(input("Número:"))
while num < 100 or num > 400:
    print(f"Valor {num} está fuera del rango")
    #recoger numero
    num = int(input("Número:"))
print(f"Valor {num} está dentro del rango")