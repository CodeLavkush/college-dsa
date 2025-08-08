"""
Practical Details
Name: Program to search the elements in the linked list and display the same.
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
            print("1.Create a LL")
            print("2.Add node to LL")
            print("3.Search")
            print("4.Display")
            print("5.Exit")
            choice = int(input("Enter your choice(1-6): "))
            match choice:
                case 1:
                    value = int(input("Enter the value: "))
                    my_ll = LinkedList(value)
                    print("LinkedList created!")
                case 2:
                    while True:
                        value = int(input("Enter the value(-1 for exit): "))
                        if value != -1:
                            my_ll.append(value)
                        else:
                            break
                case 3:
                    value = int(input("Enter the value: "))
                    print(f"Value found at {my_ll.search(value)} node")
                case 4:
                    my_ll.print_list()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()