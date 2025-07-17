"""
Practical Details
sr no. 3 & 4
Date: 26 June 2025
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            self.tail = new_node
            temp.next = new_node
        self.length += 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def search(self, value):
        if self.head is None:
            return None
        
        index = 0
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return index
            else:
                temp = temp.next
            index += 1

def main():
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Create a list")
            print("2.Add element to List")
            print("3.Search")
            print("4.Display")
            print("5.Reverse")
            print("6.Exit")
            choice = int(input("Enter your choice(1-6): "))
            match choice:
                case 1:
                    element = int(input("Enter the element: "))
                    my_ll = LinkedList(element)
                    print("LinkedList created!")
                case 2:
                    while True:
                        element = int(input("Enter the element(-1 for exit): "))
                        if element != -1:
                            my_ll.append(element)
                        else:
                            break
                case 3:
                    # This is in the practical 4
                    element = int(input("Enter the element: "))
                    print(f"Value found at {my_ll.search(element)} node") 
                case 4:
                    my_ll.print_list()
                case 5:
                    my_ll.reverse()
                case 6:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()