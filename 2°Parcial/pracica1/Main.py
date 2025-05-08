from GetNumbers import gettingNumbers
from Menu import menu


if __name__ == "__main__":
    print("Bienvenido")
    numbersList = gettingNumbers()
    menu(numbersList)

    
