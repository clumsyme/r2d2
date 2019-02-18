import os
from contextlib import contextmanager

@contextmanager
def goto(directory: str):
    cwd = os.getcwd()
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    yield None
    os.chdir(cwd)
