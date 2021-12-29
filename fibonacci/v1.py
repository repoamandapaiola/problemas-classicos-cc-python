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


# Versão com recursão infinita pois não tem um caso de base
def f1(n: int):
    return f1(n-1) + f1(n-2)


# Crescimento exponencial de chamadas,
# pois tem que fica repetindo chamadas
def f2(n: int):
    # caso de base
    if n <= 1:
        return n
    print(f"chamando {n-1} e chamando {n-2}")
    return f2(n-2) + f2(n-1)


# Usar memoização
memo = {}


def f3(n: int):
    if n not in memo:
        memo[n] = f3(n-1) + f3(n-2)
    return memo[n]

f3(10)
