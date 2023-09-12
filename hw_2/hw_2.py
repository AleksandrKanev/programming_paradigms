# Использовал процедурную и структурную парадигмы, так как не задача простая и не требовалось прибегать к другим парадигмам
def multiplication_table(n: int):
    for i in range(1, 10):
        for j in range(1, n + 1):
            if (i * j < 10):
                print(f'{j} * {i} = {i * j}', end=" " * 2)
            else:
                print(f'{j} * {i} = {i * j}', end=" ")
        else:
            print()


multiplication_table(5)
