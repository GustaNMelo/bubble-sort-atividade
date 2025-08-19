import random

def bubble_sort(lista):
    print("Lista original: ", lista)
    flag = True
    while flag:
        flag = False
        for i in range(len(lista) - 1):
            if(lista[i] > lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                flag = True
    print("Lista ordenada: ", lista)
    return lista

# Entrada manual:
entrada = input("Digite uma lista de números separados por espaço: ")
lista_usuario = list(map(int, entrada.split()))
bubble_sort(lista_usuario)

# Testes automáticos com listas maiores:
for tamanho in [10, 100, 1000]:
    print(f"\nTestando com lista de tamanho {tamanho}:")
    lista_teste = random.sample(range(1, 10000), tamanho) 
    bubble_sort(lista_teste)