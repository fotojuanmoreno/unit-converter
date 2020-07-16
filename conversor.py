import time

opciones1=["Moneda", "Distancia", "Temperatura"]
monedas = ["Euros", "Dolares"]
distancias = ["metros", "pies"]
temperaturas = ["Celsius", "Fahrenheit"]

def lista_opciones(lista):
	for i in lista:
		print(str(lista.index(i)+1) + " - " + i)

print("\nBIENVENIDO AL CONVERSOR")
print("-----------------------")
time.sleep(1)
print("¿Qué quieres convertir?")
lista_opciones(opciones1)

eleccion = int(input("\nEscribe 1, 2 o 3, dependiendo de lo que quieras: "))
time.sleep(1)
while eleccion < 1 or eleccion > 3:
	eleccion = int(input("\nEscribe 1, 2 o 3, dependiendo de lo que quieras: "))
	time.sleep(1)

if eleccion in range(1, 4):
	print("\nHas elegido: " + opciones1[eleccion-1])
	print("¿Qué " + opciones1[eleccion-1] + " quieres convertir?\n")
	if eleccion == 1:
		lista_opciones(monedas)
		seleccion = int(input("\nEscribe 1 o 2 para seleccionar: "))
		if seleccion in range(1, 3):
			print("\nHas elegido: " + monedas[seleccion-1])
			cantidad = input("¿Cuantos " + monedas[seleccion-1] + " quieres convertir a " + monedas[-seleccion] + "?: ")
			if monedas[seleccion-1] == "Euros":
				cantidad2 = float(cantidad)*1.13812
			else:
				cantidad2 = float(cantidad)*0.87864
			print("\nResultado\n")
			print(str(cantidad) + " " + monedas[seleccion-1] + " son " + str(round(cantidad2, 2)) + " " + monedas[-seleccion] + ". ")
		else:
			print("Salida en monedas")
	elif eleccion == 2:
		lista_opciones(distancias)
		seleccion = int(input("\nEscribe 1 o 2 para seleccionar: "))
		if seleccion in range(1, 3):
			print("\nHas elegido: " + distancias[seleccion-1])
			cantidad = input("¿Cuantos " + distancias[seleccion-1] + " quieres convertir a " + distancias[-seleccion] + "?: ")
			if distancias[seleccion-1] == "metros":
				cantidad2 = float(cantidad)*3.2808
			else:
				cantidad2 = float(cantidad)/3.2808
			print("\nResultado\n")
			print(str(cantidad) + " " + distancias[seleccion-1] + " son " + str(round(cantidad2, 2)) + " " + distancias[-seleccion] + ". ")
		else:
			print("Salida en distancias")
	elif eleccion == 3:
		lista_opciones(temperaturas)
		seleccion = int(input("\nEscribe 1 o 2 para seleccionar: "))
		if seleccion in range(1, 3):
			print("\nHas elegido: " + temperaturas[seleccion-1])
			cantidad = input("¿Cuantos " + temperaturas[seleccion-1] + " quieres convertir a " + temperaturas[-seleccion] + "?: ")
			if temperaturas[seleccion-1] == "Celsius":
				cantidad2 = float(cantidad)*1.8000 + 32
			else:
				cantidad2 = (float(cantidad)-32)/1.8000
			print("\nResultado\n")
			print(str(cantidad) + " grados " + temperaturas[seleccion-1] + " son " + str(round(cantidad2, 2)) + " grados " + temperaturas[-seleccion] + ". ")
		else:
			print("Salida en distancias")
else:
	print("Salida en eleccion")
