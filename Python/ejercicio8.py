peso = float(input("digite su peso en kg "))
altura = float(input("digite su estatura en metros "))

imc = peso/altura**2
print(f"su imc es: {imc}")

if imc<18.5:
    print("bajo peso")
elif imc>=18.5 and imc<25:
    print("normal")
elif imc>=25 and imc<30:
    print("sobrepeso")
elif imc>=30:
    print("sos obeso")