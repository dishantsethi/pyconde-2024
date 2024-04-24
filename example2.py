def do_something():
    pass


# bad
for _ in range(100):
    try:
        do_something()
    except Exception:
        pass


# good
try:
    for _ in range(100):
        do_something()
except Exception:
    pass
