import pytest
from catchit import *
from example1 import my_write, my_read, my_copy


def test_error_1():
    out = my_write("/etc/hosts")
    assert out == "PermissionError"


def test_error_2():
    out = my_read("/etc/a/b/c/hosts")
    assert out == "FileNotFoundError"


def test_error_3():
    out = my_copy("/a/b/c/d/e", "/a/b/c/d/e")
    assert out == "NotADirectoryError"


def test_error_4():
    pass


for number in range(1, 9):
    if number % 10 == 0:
        break
else:
    print('Lets print something out!')