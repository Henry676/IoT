from Functions import options

def menu(text):
    while True:
        while True:
            print("\n=== MENÚ ===")
            print("1. Verificar que la primera letra sea mayúscula")
            print("2. Contar palabras que forman la cadena de texto")
            print("3. Regresar lista con las palabras que conforman la cadena de texto")
            print("4. Invertir cadena de texto")
            print("5. Convertir a mayuscula el caracter final de cada palabra")
            print("6. Salir")
            try:
                option = int(input("Selecciona una opción (1-6): "))
                if 1 <= option <= 6:
                    options(option, text)
                    break
                else:
                    print("Opción inválida. Por favor, selecciona un número entre 1 y 6.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
        