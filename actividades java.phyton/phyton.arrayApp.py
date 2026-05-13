def rellenar_array(lista):
    for i in range(len(lista)):
        texto = input("Introduce un número: ")
        lista[i] = int(texto)

def mostrar_array(lista):
    for i in range(len(lista)):
        print(f"En el indice {i} esta el valor {lista[i]}")


if __name__ == "__main__":
    tamanio = 5
    num = [0] * tamanio  
    
    rellenar_array(num)  
    mostrar_array(num)    
    