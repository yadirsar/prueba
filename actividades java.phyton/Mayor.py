import random

def es_primo(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def rellenar_primos(tamano, inicio, fin):
    lista = []
    while len(lista) < tamano:
        num = random.randint(inicio, fin)
        if es_primo(num):
            lista.append(num)
    return lista

def ejecutar_programa():
    try:
       
        entrada = input("Introduce un tamaño para la lista: ")
        tamano = int(entrada)

        
        numeros = rellenar_primos(tamano, 1, 100)

       
        print("\nLista de números primos generada:")
        for indice, valor in enumerate(numeros):
            print(f"En el índice {indice} está el valor {valor}")

       
        if numeros:
            primo_mayor = max(numeros)
            print(f"\nEl primo más grande es el {primo_mayor}")
            
    except ValueError:
        print("Error: Por favor, introduce un número válido.")


ejecutar_programa()