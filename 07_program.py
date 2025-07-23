"""
Practical Details
sr no. 7
Date: 11 July 2025
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        self.max_length = 3

    def print_queue(self):
        if self.length == 0:
            print(self.isEmpty())
            return None
        
        temp = self.first
        while temp is not None:
            print(temp.value, end="\t")
            temp = temp.next
    
    def enqueue(self, value):
        if self.length >= self.max_length:
            print("Queue is full")
            return None
        
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
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
            temp.next = None
        self.length -= 1
        print(f"The value deleted is {temp.value}")

    def isEmpty(self):
        return "Queue is empty"


def main():
    while True:
        try:
            print("\n")
            print("MAIN MENU".center(24, "*"))
            print("1.Create queue")
            print("2.Insert in queue")
            print("3.Delete queue")
            print("4.Display")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    value = int(input("Enter value: "))
                    my_queue = Queue(value)
                    print("Queue created!")
                case 2:
                    value = int(input("Enter the value: "))
                    my_queue.enqueue(value)
                case 3:
                    my_queue.dequeue()
                case 4:
                    my_queue.print_queue()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()