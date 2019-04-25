recorridos = [["Ciudad 1","Ciudad 2"],["Ciudad 1","Ciudad 3","Ciudad 4"],
	["Ciudad 1","Ciudad 3","Ciudad 5","Ciudad 4"],["Ciudad 1","Ciudad 6","Ciudad 7"],["Ciudad 8"]]
def main():
	
	print(recorridos)
	print()

	#origen = 'Ciudad 4'
	origen = input("Ingrese Origen: ")
	#destino = 'Ciudad 6'
	destino = input("Ingrese Destino: ")

	conexion(origen,destino)

def conexion(a,b):
	band = 0
	for recorrido in recorridos:
		if a in recorrido and b in recorrido:
			if recorrido.index(a) <= recorrido.index(b):
				band = 1
				break

	if band == 0:
		print("No es posible viajar de {} a {}".format(a,b))
	else:
		print("Es posible viajar de {} a {}".format(a,b))


if __name__ == '__main__':
	main()


