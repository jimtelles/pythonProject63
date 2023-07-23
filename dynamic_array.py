# Name:
# OSU Email: tellesj
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date:7.16.23
# Description:


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Internal method used to increase the size of the static array inside the dynamic array.
        """
        if new_capacity <= 0 or new_capacity < self.length():
            return

        holder_array = StaticArray(new_capacity)
        for ind in range(self.length()):
            holder_array[ind] = self._data[ind]
        self._data = holder_array
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Method adds values to the end of a dynamic array.
        """
        if self.length() == self.get_capacity():
            doubler_integer = self.get_capacity() * 2
            self.resize(doubler_integer)

        self._data[self.length()] = value
        self._size += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method takes in an index position and a value, inserts the value at that index position
        in the array, and shifts the rest of the elements, from that point to the right, if the
        addition of that value, makes size of the array, match the capacity, the resize method
        is called and the array capacity is increased (doubled).
        """
        if index < 0 or index > self.length():
            raise DynamicArrayException
        elif self.length() + 1 > self.get_capacity():
            doubler_integer = self.get_capacity() * 2
            self.resize(doubler_integer)

        for ind in range(self.length() - 1, index - 1, -1):
            self._data[ind + 1] = self._data[ind]
        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Method removes an item from the indicated index position and shifts the remaining elements to the
        left to that index position. Also reduces the capacity of an array, if the number of elements
        present before reduction equal less than one quarter of the capacity, to twice the number
        of elements present. Capacity can not be reduced to below 10 regardless of the number of elements.
        """
        if index < 0 or index > self.length() - 1:
            raise DynamicArrayException

        if self.get_capacity() <= 10:
            for ind in range(index, self.length() - 1):
                self._data[ind] = self._data[ind + 1]
            self._size = self._size - 1
        elif self.length() < self.get_capacity() // 4:
            self._capacity = self.length() * 2
            for ind in range(index, self.length() - 1):
                self._data[ind] = self._data[ind + 1]
                self._size = self._size - 1
            if self.length() < self.get_capacity() // 4:
                self._capacity = self.length() * 2
                if self._capacity < 10:
                    self._capacity = 10
        else:
            for ind in range(index, self.length()):
                self._data[ind] = self._data[ind + 1]
            self._size = self._size - 1
            if self.length() < self.get_capacity() // 4:
                self._capacity = self.length() * 2
                if self._capacity < 10:
                    self._capacity = 10

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Method takes 'slices' out of an existing array, and creates a new array to hold the sliced elements. new array
        size and capacity are determined by input size.
        """
        if start_index < 0 or start_index > self.length() - 1 or self.length() - start_index < size:
            raise DynamicArrayException
        elif size == 0:
            new_array = DynamicArray()
            return new_array

        new_static_array = StaticArray(size)
        for ind in range(size):
            new_static_array[ind] = self._data[start_index]
            start_index = start_index + 1
        new_array = DynamicArray()
        while size > new_array._capacity:
            new_array._capacity = new_array._capacity * 2

        new_array._size = size
        new_array._data = new_static_array
        return new_array


    def merge(self, second_da: "DynamicArray") -> None:
        """
        Method that takes 2 arrays and appends the second one to the first.
        """
        counter = 0
        if second_da.length() + self.length() > self.get_capacity():
            doubler_integer = self.get_capacity() * 2
            self.resize(doubler_integer)

        while self._size < (second_da.length() + self.length()) and counter < second_da.length():
            self._data[self._size] = second_da[counter]
            self._size += 1
            counter = counter + 1

    def map(self, map_func) -> "DynamicArray":
        """
        Method applies a function to each element of an existing array, and outputs
        a new array with the adjusted values.
        """
        new_static_array = StaticArray(self.get_capacity())
        for ind in range(self.length()):
            new_static_array[ind] = map_func(self._data[ind])
        new_array = DynamicArray()
        new_array._size = self.length()
        new_array._capacity = self.get_capacity()
        new_array._data = new_static_array
        return new_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        Method applies a function to an array, and returns the values designated by the
        function into a new array.
        """
        i_holder = []
        b_static_array = StaticArray(self.length())
        for ind_1 in range(self.length()):
            b_static_array[ind_1] = filter_func(self._data[ind_1])
        for ind_2 in range(b_static_array.length()):
            if b_static_array[ind_2] is not True:
                i_holder.append(ind_2)
        new_array = DynamicArray()
        new_array._data = self._data
        new_array._size = self.length()
        new_array._capacity = self.length()
        for ind_3 in range(len(i_holder)):
            new_array.remove_at_index(i_holder[ind_3])

        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        TODO: Write this implementation
        """
        pass


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    # print("\n# reduce example 1")
    # values = [100, 5, 10, 15, 20, 25]
    # da = DynamicArray(values)
    # print(da)
    # print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    # print(da.reduce(lambda x, y: (x + y ** 2), -1))
    #
    # print("\n# reduce example 2")
    # da = DynamicArray([100])
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    # da.remove_at_index(0)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    #
    # print("\n# find_mode - example 1")
    # test_cases = (
    #     [1, 1, 2, 3, 3, 4],
    #     [1, 2, 3, 4, 5],
    #     ["Apple", "Banana", "Banana", "Carrot", "Carrot",
    #      "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
    #      "Fig", "Fig", "Grape"]
    # )
    #
    # for case in test_cases:
    #     da = DynamicArray(case)
    #     mode, frequency = find_mode(da)
    #     print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")
    #
    # case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    # da = DynamicArray()
    # for x in range(len(case)):
    #     da.append(case[x])
    #     mode, frequency = find_mode(da)
    #     print(f"{da}\nMode: {mode}, Frequency: {frequency}")
