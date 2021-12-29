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

# Usar memoização
memo = {0: 0, 1: 1}


def f3(n: int, c):
    if n not in memo:
        c = c + 1
        i, c = f3(n - 1, c)
        j, c = f3(n - 2, c)
        memo[n] = i + j
    return memo[n], c


if __name__ == '__main__':
    print(f3(15, 0))
