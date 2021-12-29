# Construção de Fibonacci em python
# problema da recursão

"""
Requisito de fibonacci:
A sequência é representada por:
o próximo número é a soma dos seus dois últimos,
exceto os 2 primeiros que são 0, 1
então:
0, 1, 1, 2, 3, 5, 8, 13, 21 ...
"""


# Crescimento exponencial de chamadas,
# pois tem que fica repetindo chamadas
def f2(n: int, c):
    # caso de base
    if n <= 1:
        c += 1
        return n, c
    c += 1
    i, c = f2(n - 2, c)
    j, c = f2(n - 1, c)
    return i + j, c


if __name__ == '__main__':
    print(f2(15, 0))
