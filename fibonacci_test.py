#!/bin/python3
"""
Tests for the fibonacci code example
"""
import unittest
import fibonacci
from sys import stderr
import sys


def test_prime():
    assert fibonacci.is_prime(2) == 1
    assert fibonacci.is_prime(25) == 0
    assert fibonacci.is_prime(218922995834555169026) == 0


def test_fibonacci(capsys):
    fibonacci.fibonacci(9)
    out, err = capsys.readouterr()
    assert out == "0\n1\n1\nBuzzFizz\nBuzz\nFizz\n8\nBuzzFizz\nBuzz\n34\n"
