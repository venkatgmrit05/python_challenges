from constants import *
from user_input import UserInput
from calculations import *


def main():
    input = get_user_input()

    if input == None:
        print("Exiting application")
        return
    
    answer = get_piston_result(input)
    print(f"Piston predicted to move: {answer}")


def get_user_input():
    input = UserInput()
    
    ret = input.get_material()
    if ret == False:
        print("Invalid material input")
        return None
    
    ret = input.get_shape()
    if ret == False:
        print("Invalid shape input")
        return None

    if input.shape == SPHERE or input.shape == CYLINDER or input.shape == CONE:
        ret = input.get_radius()
        if ret == False:
            print("Invalid radius input")
            return None

    if input.shape == CUBE or input.shape == CYLINDER or input.shape == CONE:
        ret = input.get_height()
        if ret == False:
            print("Invalid height input")
            return None
        
    ret = input.get_p1()
    if ret == False:
        print("Invalid pressure value")
        return None
    
    ret = input.get_p2()
    if ret == False:
        print("Invalid pressure value")
        return None
        
    return input


def get_piston_result(input):
    volume_of_item = get_volume(input)
    mass_of_item = get_mass(input.shape, volume_of_item)
    weight_of_item = get_weight(mass_of_item)
    upwward_force_on_piston = get_upward_force_on_piston(input.p1, input.p2)
    
    if upwward_force_on_piston > weight_of_item:
        return "Up"
    elif upwward_force_on_piston == weight_of_item:
        return "Neutral"
    else:
        return "Down"


if __name__ == "__main__":
    main()