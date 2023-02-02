#def Conversor(tipo_pesos, valor_dolar):
    

menu = """
Bienvenido al conversor de moneras 💕(●'◡'●)

1 - Pesos Colombianos
2 - Pesos Argenitos
3 - Pesos Mexicanos
Elige una opcion: """

opcion = input(menu)

if opcion == "1":
    pesos = input ("¿Cuantos pesos colombianos tienes?: ")
    pesos = float (pesos)
    valor_dolar = 4777
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == "2":
    pesos = input ("¿Cuantos pesos argentinos tienes?: ")
    pesos = float (pesos)
    valor_dolar = 173
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == "3":
    pesos = input ("¿Cuantos pesos mexicanos tienes?: ")
    pesos = float (pesos)
    valor_dolar = 19.73
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print("Tienes $" + dolares + " dolares")
else: 
    print("Ingresa una opción correcta, por favor")



