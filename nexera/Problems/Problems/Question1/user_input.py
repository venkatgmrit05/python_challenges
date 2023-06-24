from input_checker import *
from constants import *

class UserInput():
    def __init__(self):
        self.material = None
        self.shape = None
        self.radius = None
        self.height = None
        self.unit = None
        self.p1 = None
        self.p2 = None

    def get_material(self):
        print("Please enter the index for the item material:")
        print("0 - Oak")
        print("1 - Aluminum")
        print("2 - Paper")
        print("3 - Stainless Steel")
        print("4 - Polystyrene")
        print()
        
        try:
            material = int(input())
        except: 
            return False
        
        if is_valid_material(material):
            self.material = material
            return True
        
        self.material = None
        return False
    

    def get_shape(self):
        print()
        print("Please enter the index for the item shape:")
        print("0 - Cube")
        print("1 - Sphere")
        print("2 - Cylinder")
        print("3 - Cone")
        print()

        try:
            shape = int(input())
        except: 
            return False
        
        if is_valid_shape(shape):
            self.shape = shape       
            return True
        
        self.shape = None
        return False


    def get_radius(self):
        print()
        print("Please enter the radius for the item:")
        print()

        try:
            radius = int(input())
        except: 
            return False
        
        if is_valid_dimension(radius):
            self.radius = radius
            return True
        
        self.radius = None
        return False
    

    def get_height(self):
        print()
        print("Please enter the height for the item:")
        print()

        try:
            height = float(input()) 
        except: 
            return False
        
        if is_valid_dimension(height):
            self.height = height
            return True
        
        self.height = None
        return False


    def get_p1(self):
        print()
        print("Please enter p1")
        print()

        try:
            p1 = float(input()) 
        except: 
            return False
        
        self.p1 = p1
        return True
    

    def get_p2(self):
        print()
        print("Please enter p2")
        print()

        try:
            p2 = float(input())
        except: 
            return False
        
        self.p2 = p2
        return True

        
