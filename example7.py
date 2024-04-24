def get_set_delete_fn(obj):
    pass


# bad
import timeit


class NotSlotted(object):
    foo: str


not_slotted = NotSlotted()

min(timeit.repeat(get_set_delete_fn(not_slotted)))
# >> 0.10123675000022558

# good
import timeit


# faster data access
class Slotted(object):
    foo: str
    __slots__ = "foo"


slotted = Slotted()

min(timeit.repeat(get_set_delete_fn(slotted)))
# >> 0.08520045899990691
