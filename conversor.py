import time

opciones1=["Moneda", "Distancia", "Temperatura"]
monedas = ["Euros", "Dolares"]
distancias = ["metros", "pies"]
temperaturas = ["Celsius", "Fahrenheit"]

def lista_opciones(lista):
	for i in lista:
		print(str(lista.index(i)+1) + " - " + i)

print("BIENVENIDO AL CONVERSOR")
print("-----------------------")
time.sleep(1)
print("¿Qué quieres convertir?")
lista_opciones(opciones1)

eleccion = input("\nEscribe 1, 2 o 3, dependiendo de lo que quieras: ")
time.sleep(1)

if eleccion == "1":
	print("\nHas elegido: " + opciones1[0])
	print("¿Qué " + opciones1[0] + " quieres convertir?\n")
	lista_opciones(monedas)
elif eleccion == "2":
	print("\nHas elegido: " + opciones1[1])
	print("¿Qué " + opciones1[1] + " quieres convertir?\n")
	lista_opciones(distancias)
elif eleccion == "3":
	print("\nHas elegido: " + opciones1[2])
	print("¿Qué " + opciones1[2] + " quieres convertir?\n")
	lista_opciones(temperaturas)