# bad
res = []
for i in range(100_000):
    if i % 2 == 0:
        res.append(i)


# good
res = [i for i in range(100_000) if i % 2 == 0]
