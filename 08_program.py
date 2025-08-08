"""
Practical Details
Name: Program to implement the concept of circular queue.
sr no. 8
Date: 11 July 2025
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueue:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.first = new_node
        self.last = new_node
        self.length = 1
        self.max_length = 4

    def print_queue(self):
        if self.length == 0:
            print(self.isEmpty())
            return None

        temp = self.first
        for _ in range(self.length):
            print(temp.value, end="\t")
            temp = temp.next

    def enqueue(self, value):
        if self.length >= self.max_length:
            print("Queue is full")
            return None
        
        new_node = Node(value)
        if self.length == 0:
            new_node.next = new_node
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        print("Succesfully Inserted")

    def dequeue(self):
        if self.length == 0:
            print(self.isEmpty())
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            self.last.next = self.first
            temp.next = None
        self.length -= 1
        print(f"The value deleted is {temp.value}")
    
    def isEmpty(self):
        return "Queue is empty"


def main():
    while True:
        try:
            print("\t")
            print("MAIN MENU".center(24, "*"))
            print("1.Create circular queue")
            print("2.Insert in circular queue")
            print("3.Delete circular queue")
            print("4.Display")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    value = int(input("Enter value: "))
                    my_Circularqueue = CircularQueue(value)
                    print("Queue created!")
                case 2:
                    value = int(input("Enter the value: "))
                    my_Circularqueue.enqueue(value)
                case 3:
                    my_Circularqueue.dequeue()
                case 4:
                    my_Circularqueue.print_queue()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()