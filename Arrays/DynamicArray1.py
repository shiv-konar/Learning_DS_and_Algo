class DynamicArray1(object):
    """Implementation of Dynamic Array type data structure which internally uses a dictionary
    Implements all methods found in Python List except sort and reverse

    Attributes
    ----------
    length : int
        the length of the dynamic array
    Methods
    -------
    length()
        Returns the length of the dynamic array

    pop()
        Removes and returns the last element in the dynamic array

    append(item)
        Adds the item to the end of the dynamic array

    get_item(index)
        Returns the element at location specified by index

    index(item)
        Returns the index of the item

    insert(index,item)
        Adds the new item at location specified by index

    remove(item)
        Removes the item from the dynamic array, if found, else raises ValueError

    count(item)
        Returns the number of occurrences of the item in the dynamic array

    extend(other_dynamic_array)
        Returns a new dynamic array which is formed by appending the parameter to the existing dynamic array

    copy()
        Returns a new dynamic array which is a copy of the existing one

    clear()
        Removes all the items in the dynamic array
    """
    def __init__(self):
        self._data = {}

    def __len__(self):
        return len(self._data)

    @property
    def length(self):
        return self.__len__()

    def pop(self):
        item = self._data[self.length - 1]
        del self._data[self.length - 1]
        return item

    def append(self, item):
        self._data[self.length] = item

    def __getitem__(self, index):
        try:
            return self._data[index]
        except KeyError:
            raise IndexError("Index out of bounds")

    def get_item(self, index):
        self.__getitem__(index)

    def index(self, item):
        for k, v in self._data.items():
            if v == item:
                return k
        raise ValueError("{0} not in the dynamic list".format(item))

    def insert(self, index, item):
        if index > self.length:
            self.append(item)
        else:
            for i in range(index + 1, self.length + 1):
                self._data[i] = self._data[i - 1]
            self._data[index] = item

    def remove(self, item):
        found_at = None
        for k,v in self._data.items():
            if v == item:
                found_at = k
        if found_at:
            if found_at == self.length - 1:
                del self._data[found_at]
            else:
                for i in range(found_at, self.length):
                    self._data[i] = self._data[i+1]
                del self._data[self.length - 1]
        else:
            raise ValueError("{0} not in the dynamic list".format(item))

    def __repr__(self):
        return "[" + ','.join(self._data.values()) + "]"

    def count(self, item):
        item_count = 0
        for v in self._data.values():
            if v == item:
                item_count += 1
        return item_count

    def extend(self, another_list):
        for item in another_list:
            self.append(item)

    def copy(self):
        array_copy = DynamicArray1()
        for k, v in self._data:
            array_copy._data[k] = v
        return array_copy

    def clear(self):
        for k in self._data.keys():
            del self._data[k]


def main():
    if __name__ == '__main__':
        array1 = DynamicArray1()  # instantiate a new dynamic array
        print(len(array1))
        # print(array1.length())
        print(array1)
        print("######################")
        array1.append('a')
        array1.append('b')
        array1.append('c')
        print(array1)
        array1.pop()
        print(array1)
        print(array1.count('z'))
        print(array1.count('b'))

main()