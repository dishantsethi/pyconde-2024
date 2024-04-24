# bad
def add(x: int, y: int):
    return x + y


x = 1
for i in range(100_000):
    add(i, x)


# good
x = 1
for i in range(100_000):
    i + x
