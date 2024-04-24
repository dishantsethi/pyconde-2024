# bad
from dataclasses import dataclass


@dataclass
class myClass:
    foo: str
    bar: str


for _ in range(100000):
    obj = myClass("foo", "bar")
    str(obj)

# >> 00:00:00:114

# good
from collections import namedtuple

myClass = namedtuple("myClass", ["foo", "bar"])

for _ in range(100000):
    obj = myClass("foo", "bar")
    str(obj)

# >> 00:00:00:59
