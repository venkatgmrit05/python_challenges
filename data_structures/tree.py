class Node:
    
    def __init__(self,
                 data,
                 left=None,
                 right=None):
        
        self.left = left
        self.right = right
        self.data = data
    
    def __str__(self):
        return str(self.data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
            
        print(self.data)

        if self.right:
            self.right.print_tree()
            


    def insert(self,data):
        if not self.data == None:
            if data < self.data :
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data :
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
