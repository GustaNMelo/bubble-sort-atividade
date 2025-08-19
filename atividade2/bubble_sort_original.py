def bubble_sort_original(lista):
    n = len(lista)
    iteracoes = 0
    for _ in range(n):
        for i in range(n - 1):
            iteracoes += 1
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return iteracoes
