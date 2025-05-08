from Functions import options

def menu(numbersList):
    while True:
        while True:
            print("\n=== MENÚ ===")
            print("1. Mostrar sublista con los 2 elementos centrales")
            print("2. Mostrar primer y último elemento")
            print("3. Duplicar lista y mostrar resultado")
            print("4. Ordenar de menor a mayor")
            print("5. Ordenar de mayor a menor")
            print("6. Cubo de cada elemento de la lista")
            print("7. Mostrar lista")
            print("8. Cambiar numeros de la lista")
            print("9. Salir")
            try:
                option = int(input("Selecciona una opción (1-9): "))
                if 1 <= option <= 9:
                    options(option, numbersList)
                    break
                else:
                    print("Opción inválida. Por favor, selecciona un número entre 1 y 9.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
        