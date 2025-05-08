def gettingNumbers():
    print("De cuantos valores quieres hacer la lista?")    
    numbers_to_add = int(input())
    numbers = []
    for i in range(numbers_to_add):
        number = int(input(f"Agregando valor {i + 1}: "))
        numbers.append(number)
        print(f"Numero {number} añadido a la lista.")
    print("Numeros agregados a la lista:")
    for number in numbers:
        print(number)
    return numbers