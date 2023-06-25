from constants import *
from user_input import UserInput
from calculations import *
import os


# XXX :comments: methods for debugging
def get_inputs_csv(fp):

    all_inputs = []
    with open(fp, 'r') as file:
        ins = file.readlines()

    for i in ins:
        j = i.strip().split('\t')
        # print(i)
        # print('\t\t', j)
        all_inputs.append(j)
    return all_inputs

#


def get_user_input_():

    materials = {
        'OAK': 0,
        'ALUMINUM': 1,
        'PAPER': 2,
        'STAINLESS_STEEL': 3,
        'POLYSTYRENE': 4,
    }

    shapes = {
        'CUBE': 0,
        'SPHERE': 1,
        'CYLINDER': 2,
        'CONE': 3,
    }

    input = UserInput()

    # fp = r'D:\Data\OfficeWorkspace-20191016T044923Z-001\OfficeWorkspace'\
    #     r'\python_challenges\nexera\Problems\Problems\Question1\probem_inputs.csv'
    fp = os.path.join(os.path.dirname(__file__), 'probem_inputs.csv')

    all_inputs = get_inputs_csv(fp)

    i = 6
    ins = all_inputs[i]

    input.material = materials[ins[0].upper()]
    input.shape = shapes[ins[1].upper()]
    input.colour = ins[2]
    if ins[3] != 'None':
        input.radius = float(ins[3])
    if ins[4] != 'None':
        input.height = float(ins[4])
    input.unit = ins[5]
    input.p1 = float(ins[6])
    input.p2 = float(ins[7])

    return input

# ---org---


def main():
    input = get_user_input()
    # input = get_user_input_()  # XXX :comments: use for debugging

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
    print('material:: ', input.material)
    print('shape::', input.shape)
    print('radius::', input.radius)
    print('height::', input.height)
    print('unit::', input.unit)
    print('p1::', input.p1)
    print('p2::', input.p2)

    volume_of_item = get_volume(input)
    # mass_of_item = get_mass(input.shape, volume_of_item)
    # # XXX replaced incorrect arguments
    mass_of_item = get_mass(input.material, volume_of_item)
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

    # I have placed XXX notations at places of corrected code and comments.

    # Notes: I added a couple of methods to help with easier debugging.
    # remvove the '_' at the end of the method get_user_input0() in line 76
    # to revert to original form of the code.

    # Notes:  I am fairly certain the rows 8 and 9[index 6 and 7] Q1 excel
    # may be incorrect in their defintion
    # of whether the piston should go up or down
    # I have also included a quick cross checker jupyter notebook.
    # my code predicts it should go up for index 6 and down for index 7
