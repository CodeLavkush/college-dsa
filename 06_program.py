"""
Practical Details
Name: Program to implement the concept of stack 
with push, pop, Display and Exit operations.
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
        if self.length == 0:
            print(self.isEmpty())
            return None
        
        temp = self.top
        while temp is not None:
            print(temp.value, end="\t")
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
        if self.length == 0:
            print(self.isEmpty())
            return None
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1
        print("Value successfully poped")

    def peek(self):
        if self.length == 0:
            print(self.isEmpty())
            return None
        else:
            return self.top
    
    def isEmpty(self):
        return "Stack is empty"


def main():
    while True:
        try:
            print("\n")
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
                    value = int(input("Enter the value: "))
                    my_stack = Stack(value)
                    print("Stack created!")
                case 2:
                    value = int(input("Enter the value: "))
                    my_stack.push(value)
                    print("Value successfully pushed")
                case 3: 
                    my_stack.pop()
                case 4:
                    print("The topmost element is: ", my_stack.peek().value)
                case 5:
                    my_stack.print_stack()
                case 6:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()