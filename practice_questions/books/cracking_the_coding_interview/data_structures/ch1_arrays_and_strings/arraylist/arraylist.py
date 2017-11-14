"""
@author: David Lei
@since: 21/08/2016
@modified: 

"""

class ArrayList:
    def __init__(self, start_size):
        self.arr = ['`'] *start_size
        self.pointer = 0    # next free index

    def add(self, element):
        self.arr[self.pointer] = element
        self.pointer += 1
        if self.pointer >= self.get_size():
            self._resize()

    def get_size(self):
        return len(self.arr)

    def _resize(self):
        for _ in range(self.get_size()):
            self.arr.append('~')
        print("Array resized " + str(self.arr))

if __name__ == "__main__":
    al = ArrayList(4)
    al.add(1)
    al.add(2)
    al.add(3)
    al.add(4)
    al.add(5)
    print(al.arr)