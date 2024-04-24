# bad
x = ["Pycon", "de", "&", "Pydata", "berlin"]
for i in range(100_000):
    len(x) + 1


# good
x = ["Pycon", "de", "&", "Pydata", "berlin"]
j = len(x)
for i in range(100_000):
    j + 1
