# Name:Jim Telles
# OSU Email:tellesj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:3
# Due Date:7.24.23
# Description:linked lists, stacks, queue, deque.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Method inserts always inserts a value right after the head or sentinel node at the front
        of the single linked list.
        """
        new_node = SLNode(value)
        if self._head.next is not None:
            new_node.next = self._head.next
            self._head.next = new_node
        else:
            self._head.next = new_node
            new_node.next = None

    def insert_back(self, value: object) -> None:
        """
        Method adds to the end of a linked list. If the list is empty, it adds a node
        after the head. If the list is not empty, it travels from node to node until
        node.next = None, and then adds the new node, and points the new_node.next to
        None.
        """
        new_node = SLNode(value)
        if self._head.next is None:
            self._head.next = new_node
            new_node.next = None
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = None

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method takes in an index position, runs a for loop until it hits that index number
        in the linked list, and inserts a value at that point.
        """
        length = self.length()
        if index < 0 or index > length:
            raise SLLException

        current_node = self._head
        for i in range(index):
            current_node = current_node.next
        temp = SLNode(value)
        temp.next = current_node.next
        current_node.next = temp

    def remove_at_index(self, index: int) -> None:
        """
        Method removes a node from the index position passed in.
        """
        length = self.length()
        if index < 0 or index > length - 1:
            raise SLLException

        current_node = self._head
        for i in range(index):
            current_node = current_node.next
        current_node.next = current_node.next.next

    def remove(self, value: object) -> bool:
        """
        Method scans entire list for a value, and if that value is found, removes the first
        occurrence of that value, and returns True, else it returns False if that value is
        not found in the linked list.
        """
        initial_length = self.length()
        new_length = initial_length
        index_holder = []
        boolean_holder = []
        current = self._head
        for ind_1 in range(self.length()):
            current = current.next
            if current.value == value:
                boolean_holder.append(True)
            else:
                boolean_holder.append(False)
        for ind_2 in range(self.length()):
            if boolean_holder[ind_2]:
                index_holder.append(ind_2)
        if not index_holder:
            return False
        else:
            self.remove_at_index(index_holder[0])
        new_length = self.length()
        if new_length < initial_length:
            return True
        else:
            return False

    def count(self, value: object) -> int:
        """
        Method scans the linked list for a value, and if that value is found,
        returns the number of times it appears in the list.
        """
        index_holder = []
        boolean_holder = []
        current = self._head
        for ind_1 in range(self.length()):
            current = current.next
            if current.value == value:
                boolean_holder.append(True)
            else:
                boolean_holder.append(False)
        for ind_2 in range(self.length()):
            if boolean_holder[ind_2]:
                index_holder.append(ind_2)
        if not index_holder:
            return 0
        else:
            count = 0
            for ind_3 in range(len(index_holder)):
                count = count + 1
            return count

    def find(self, value: object) -> bool:
        """
        Method scans the linked list for a value, if found, returns True, if not found
        returns False.
        """
        index_holder = []
        boolean_holder = []
        current = self._head
        for ind_1 in range(self.length()):
            current = current.next
            if current.value == value:
                boolean_holder.append(True)
            else:
                boolean_holder.append(False)
        for ind_2 in range(self.length()):
            if boolean_holder[ind_2]:
                index_holder.append(ind_2)
        if not index_holder:
            return False
        else:
            return True

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        if start_index < 0 or start_index + size > self.length():
            raise SLLException
        new_linked_list = LinkedList()
        new_linked_list._head = self._head
        current = new_linked_list._head
        if size == self.length():
            new_linked_list._head.next = None
            return new_linked_list
        else:
            for ind in range(self.length()):
                current = current.next
            current = new_linked_list._head
            for ind_2 in range(size):
                current = current.next
            current.next = None
            current = new_linked_list._head
            for ind_3 in range(start_index):
                current = current.next
            new_linked_list._head.next = current
            return new_linked_list








if __name__ == "__main__":

    # print("\n# insert_front example 1")
    # test_case = ["A", "B", "C"]
    # lst = LinkedList()
    # for case in test_case:
    #     lst.insert_front(case)
    #     print(lst)
    #
    # print("\n# insert_back example 1")
    # test_case = ["C", "B", "A"]
    # lst = LinkedList()
    # for case in test_case:
    #     lst.insert_back(case)
    #     print(lst)
    #
    # print("\n# insert_at_index example 1")
    # lst = LinkedList()
    # test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    # for index, value in test_cases:
    #     print("Inserted", value, "at index", index, ": ", end="")
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print("\n# remove_at_index example 1")
    # lst = LinkedList([1, 2, 3, 4, 5, 6])
    # print(f"Initial LinkedList : {lst}")
    # for index in [0, 2, 0, 2, 2, -2]:
    #     print("Removed at index", index, ": ", end="")
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print("\n# remove example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [7, 3, 3, 3, 3]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# remove example 2")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# count example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    # print("\n# find example 1")
    # lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    # print(lst)
    # print(lst.find("Waldo"))
    # print(lst.find("Superman"))
    # print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
