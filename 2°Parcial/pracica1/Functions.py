from GetNumbers import gettingNumbers 


def cubo(x):
    return x**3

def options(option, numbersList):
    if option == 1:
        half = len(numbersList) // 2
        print("Sublista con los 2 elementos centrales:", numbersList[half-1:half+1])
    elif option == 2:
        print("Primer elemento:", numbersList[0])
        print("Último elemento:", numbersList[-1])
    elif option == 3:
        print("Lista duplicada:", numbersList * 2)
    elif option == 4:
        print("Lista ordenada de menor a mayor:", sorted(numbersList))
    elif option == 5:
        print("Lista ordenada de mayor a menor:", sorted(numbersList, reverse=True))
    elif option == 6:
        print("Cubo de cada elemento:",list(map(cubo,numbersList)))
    elif option == 7:
        print("Lista actual:", numbersList)
    elif option == 8:
        numbersList[:] = gettingNumbers()
    elif option == 9:
        print("Saliendo del programa.")
        exit()