import pytest

from toolkit.calculator import calculate


def test_add():
    assert calculate("2+2") == 4

def test_priority():
    assert calculate("2+2*2") == 6

def test_parens():
    assert calculate("(1+1)*2") == 4

def test_unary_minus():
    assert calculate("-5+3") == -2

def test_float():
    assert calculate("3.5+1.5") == 5.0

def test_empty():
    with pytest.raises(ValueError):
        calculate("")

def test_double_op():
    with pytest.raises(ValueError):
        calculate("2**3")

def test_unbalanced():
    with pytest.raises(ValueError):
        calculate("(1+1")

def test_double_nums():
    with pytest.raises(ValueError):
        calculate("1*(2+3 4)")