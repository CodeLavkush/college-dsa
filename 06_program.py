"""
Practical Details
sr no. 6
Date: 3 July 2025
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1

    def peek(self):
        if self.length == 0:
            return None
        
        return self.top

def main():
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Create Stack")
            print("2.Push")
            print("3.Pop")
            print("4.Peek")
            print("5.Display")
            print("6.Exit")
            choice = int(input("Enter your choice(1-6): "))
            match choice:
                case 1:
                    element = int(input("Enter value: "))
                    my_stack = Stack(element)
                    print("Stack created!")
                case 2:
                    while True:
                        element = int(input("Enter the element(-1 for exit): "))
                        if element != -1:
                            my_stack.push(element)
                        else:
                            break
                case 3: 
                    my_stack.pop()
                case 4:
                    print(my_stack.peek().value)
                case 5:
                    my_stack.print_stack()
                case 6:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()