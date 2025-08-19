def bubble_sort_otimizado(lista):
    n = len(lista)
    iteracoes = 0
    for _ in range(n):
        trocou = False
        for i in range(n - 1):
            iteracoes += 1
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True
        if not trocou:
            break
    return iteracoes
