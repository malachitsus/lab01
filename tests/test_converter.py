import pytest

from toolkit.converter import convert


def test_km_to_m():
    assert convert(5, 'km', 'm') == 5000

def test_m_to_km():
    assert convert(5000, 'm', 'km') == 5

def test_c_to_f():
    assert convert(100, 'c', 'f') == 212

def test_kg_to_g():
    assert convert(2, 'kg', 'g') == 2000

def test_incompatible():
    with pytest.raises(ValueError):
        convert(5, 'kg', 'km')

def test_unknown_unit():
    with pytest.raises(ValueError):
        convert(5, 'xyz', 'm')

def test_below_absolute_zero():
    with pytest.raises(ValueError):
        convert(-300, 'c', 'f')