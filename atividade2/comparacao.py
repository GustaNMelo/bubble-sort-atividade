import random
import time
from bubble_sort_original import bubble_sort_original
from bubble_sort_otimizado import bubble_sort_otimizado

tamanhos = [10, 100, 1000]

for tamanho in tamanhos:
    print(f"\n--- Lista de tamanho {tamanho} ---")
    
    lista_base = random.sample(range(1, 10000), tamanho)

    # Versão original
    lista1 = lista_base.copy()
    start = time.time()
    iteracoes1 = bubble_sort_original(lista1)
    tempo1 = time.time() - start
    print(f"Original - Iterações: {iteracoes1}, Tempo: {tempo1:.4f} s")

    # Versão otimizada
    lista2 = lista_base.copy()
    start = time.time()
    iteracoes2 = bubble_sort_otimizado(lista2)
    tempo2 = time.time() - start
    print(f"Otimizado - Iterações: {iteracoes2}, Tempo: {tempo2:.4f} s")
