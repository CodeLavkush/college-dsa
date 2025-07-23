"""
Practical Details
sr no. 5
Date: 3 July 2025
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next
        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp

def main():
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Create Double LL")
            print("2.Add value to DLL")
            print("3.Display")
            print("4.Sort")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    value = int(input("Enter the value: "))
                    my_double_LL = DoubleLL(value)
                    print("Double LL created!")
                case 2:
                    while True:
                        value = int(input("Enter the value(-1 for exit): "))
                        if value != -1:
                            my_double_LL.append(value)
                        else:
                            break
                case 3: 
                    my_double_LL.print_dll()
                case 4:
                    my_double_LL.bubble_sort()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()