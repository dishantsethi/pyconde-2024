# bad
def with_kwargs(**kwargs):
    return kwargs.get("a") + kwargs.get("b")


with_kwargs(a=1, b=2)


# good
def without_kwargs(a: int, b: int):
    return a + b


without_kwargs(a=1, b=2)
