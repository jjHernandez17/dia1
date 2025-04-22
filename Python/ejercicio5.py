
total_cuenta= float(input("digite el total de la cuenta: "))

propina = float(input("diga que porcentaje del total de la cuenta desea dejar de propina (10%, 15%, 20%)"))

if propina==10:
    total_propina = (total_cuenta/100)*10
    print(f"la propina es:  {total_propina}")
elif propina==15:
    total_propina = (total_cuenta/100)*15
    print(f"la propina es:  {total_propina}")
elif propina==20:
    total_propina = (total_cuenta/100)*20
    print(f"la propina es:  {total_propina}")
else: 
    print("el porcentaje de propina no es valido")