opciones1=["Moneda", "Distancia", "Temperatura"]
monedas = ["Euros", "Dolares"]
distancias = ["metros", "pies"]
temperaturas = ["Celsius", "Fahrenheit"]

def main():
	print("\nBIENVENIDO AL CONVERSOR")
	print("-----------------------")
	print("\n¿Qué quieres convertir?")
	lista_opciones(opciones1)

	eleccion = int(input("\nEscribe 1, 2 o 3, dependiendo de lo que quieras: "))
	while eleccion < 1 or eleccion > 3:
		eleccion = int(input("\nEscribe 1, 2 o 3, dependiendo de lo que quieras: "))
	if eleccion in range(1, 4):
		print("\nHas elegido: " + opciones1[eleccion-1])
		print("¿Qué " + opciones1[eleccion-1] + " quieres convertir?\n")
		if eleccion == 1:
			categoria = monedas
		elif eleccion == 2:
			categoria = distancias
		elif eleccion == 3:
			categoria = temperaturas
		conversor(categoria)
	else:
		print("Salida en eleccion")

def lista_opciones(lista):
	for i in lista:
		print(str(lista.index(i)+1) + " - " + i)

def conversor(categoria):
	lista_opciones(categoria)
	seleccion = int(input("\nEscribe 1 o 2 para seleccionar: "))
	if seleccion < 1 or seleccion> 2:
		while seleccion < 1 or seleccion> 2:
			seleccion = int(input("\nEscribe 1 o 2 para seleccionar: "))
	if seleccion in range(1, 3):
		print("\nHas elegido: " + categoria[seleccion-1])
		cantidad = input("¿Cuantos " + categoria[seleccion-1] + " quieres convertir a " + categoria[-seleccion] + "?: ")
		operaciones(categoria, seleccion, cantidad)
		print("\nResultado\n")
		print(str(cantidad) + " " + categoria[seleccion-1] + " son " + str(round(cantidad2, 2)) + " " + categoria[-seleccion] + ". ")
		print("\n¿Quieres realizar otra operación?\n")
		cierre = input("y/n: ")
		while cierre != "y" and cierre != "n":
			print("\n¿Quieres realizar otra operación?\n")
			cierre = input("y/n: ")
		cierre = cierre.lower()
		if cierre == "y":
			main()
		else:
			print("\nHasta la próxima.")
			exit()
	else:
		print("Algo no ha ido bien. \nReiniciame.")

def operaciones(categoria, seleccion, cantidad):
	global cantidad2
	if categoria[seleccion-1] == "Euros":
		cantidad2 = float(cantidad)*1.13812
	elif categoria[seleccion-1] == "Dolares":
		cantidad2 = float(cantidad)*0.87864
	elif categoria[seleccion-1] == "metros":
		cantidad2 = float(cantidad)*3.2808
	elif categoria[seleccion-1] == "pies":
		cantidad2 = float(cantidad)/3.2808
	elif categoria[seleccion-1] == "Celsius":
		cantidad2 = float(cantidad)*1.8000 + 32
	elif categoria[seleccion-1] == "Fahrenheit":
		cantidad2 = (float(cantidad)-32)/1.8000


if __name__ == '__main__':
	main()