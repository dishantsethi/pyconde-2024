# bad
import os

for _ in range(100):
    os.path.exists("/")

# good
from os.path import exists

for _ in range(100):
    exists("/")
