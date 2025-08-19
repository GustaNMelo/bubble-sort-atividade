# Atividade 2 – Otimização do Algoritmo Bubble Sort

Esta atividade tem como objetivo implementar uma **versão otimizada do Bubble Sort**, que interrompe a ordenação caso nenhuma troca ocorra durante uma iteração, evitando comparações desnecessárias.

---

## 📄 Arquivos

- `bubble_sort_original.py`: implementação sem otimização.
- `bubble_sort_otimizado.py`: implementação com verificação de trocas.
- `comparacao.py`: executa testes comparando as duas versões.

---

## 🧪 Testes Realizados

Foram testadas listas de tamanhos:

- 10
- 100
- 1000

Cada teste mede:

- Número de iterações (quantas comparações foram feitas)
- Tempo total de execução

---

## 📊 Resultados esperados

```plaintext
--- Lista de tamanho 100 ---
Original - Iterações: 9900, Tempo: 0.1350 s
Otimizado - Iterações: 5400, Tempo: 0.0685 s
