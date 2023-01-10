# from collections import list

class Stack(list):

    def __init__(self):
        super(Stack, self).__init__()

        self._data = list()
        self.data = self._data

# class Stack:
#     """
#     LIFO
#     """
#     def __init__(self):
#         # super(Stack, self).__init__()
#         self._data = []
#         self.data = self._data

    def __repr__(self):
        return f"{self._data}"

    def __str__(self):
        return f"{self._data}"

    def push(self, item):
        self._data.append(item)

    def pop(self):
        top_element = self._data.pop(-1)
        return top_element

    def top(self):
        try:
            return self._data[-1]
        except IndexError as e:
            print(f"index error: {e}")

    def is_empty(self):

        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":

    s = Stack()
    arr = [1, 2, 3, 4, 5, 6]
    print(s)
    s.push(6)

    # a= list()

    print('done')
