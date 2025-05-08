

def cubo(x):
    return x**3

def options(option, text):
    if option == 1:
        if(text[0].isupper()):
            print("La primera letra es mayúscula")
            return True
        else:
            print("La primera letra no es mayúscula")
            return False
    elif option == 2:
        words = text.split()
        print("Número de palabras:", len(words))
    elif option == 3:
        words = []
        words = text.split()
        print("Lista de palabras:", words)
    elif option == 4:
        print("Texto invertido:", text[::-1])
    elif option == 5:
        print("Caracter final de cada palabra convertida en mayuscula: ", end="")
        words = text.split()
        for word in words:
            print(word[:-1] + word[-1].upper(), end=" ")
        print() 
    elif option == 6:
        print("Saliendo del programa.")
        exit()