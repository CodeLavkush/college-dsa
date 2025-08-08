"""
Practical Details
Name: Program to create a single linked list and display 
the node elements in reverse order.
sr no. 3
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

def main():
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Create a LL")
            print("2.Add node to LL")
            print("3.Display")
            print("4.Reverse")
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
                    my_ll.print_list()
                case 4:
                    my_ll.reverse()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()