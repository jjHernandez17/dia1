numero = 4
adivina = 0
a=11

for intentos in range(a):
    a=a-1
    adivina = int(input(f"divina el numero tienes  {a} intentos"))
    if adivina>numero:
        print("el numero es menor al tuyo")
    elif adivina<numero:
        print("el numero es mayor al tuyo")
    else:
       print("haz adivinado el numero¡¡¡¡")
       break


