import math
from constants import *


def get_volume(input):
    if input.shape == CUBE:
        return get_volume_of_cube(input.height)
    elif input.shape == SPHERE:
        return get_volume_of_sphere(input.radius)
    elif input.shape == CYLINDER:
        return get_volume_of_cylinder(input.radius, input.height)
    elif input.shape == CONE:  # XXX
        return get_volume_of_cone(input.radius, input.height)


def get_volume_of_cube(height):
    return height ** 3


def get_volume_of_sphere(radius):
    return 4.0 / 3.0 * math.pi * (radius ** 3)


def get_volume_of_cylinder(radius, height):
    return math.pi * (radius ** 2) * height


def get_volume_of_cone(radius, height):
    return math.pi * (radius ** 2) * height / 3.0


def get_mass(material, volume):
    density = DENSITIES[material]
    print(material)
    print(DENSITIES)
    print(density, '----', volume)
    return density * volume


def get_weight(mass):
    return mass * GRAVITY_MS2


def get_upward_force_on_piston(p1, p2):
    # delta_p = p1-p2  # org XXX
    delta_p = abs(p1-p2)  # TODO XXX check which of these is right
    return AREA_OF_PISTON * delta_p
