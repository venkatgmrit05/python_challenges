def is_valid_material(material):
    return material >= 0 and material <=4

def is_valid_shape(shape):
    return shape >= 0 and shape <= 3

def is_valid_dimension(dim):
    return dim > 0.0

def is_valid_unit(unit):
    return unit == "i" or unit == "m"