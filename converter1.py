MASS = {'kg': 1, 'g': 1000}
LENGTHS = {'km': 0.001, 'm': 1, 'cm': 100, 'mm': 1000}
TEMPERATURES = {'c', 'k', 'f'}

def get_group(unit):
    if unit in LENGTHS:
        return 'length'
    if unit in MASS:
        return 'mass'
    if unit in TEMPERATURES:
        return 'temp'
    raise ValueError(f"unknown unit: {unit}")

def to_celsius(value, unit):
    if unit == 'c':
        return value
    if unit == 'k':
        return value - 273.15
    if unit == 'f':
        return (value - 32) * 5 / 9
    else:
        raise ValueError(f"unknown temp unit: {unit}")

def from_celsius(celsius, unit):
    if unit == 'c':
        return celsius
    if unit == 'k':
        return celsius + 273.15
    if unit == 'f':
        return celsius * 9 / 5 + 32 
    else:
        raise ValueError(f"unknown temp unit: {unit}")

