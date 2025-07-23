"""
Practical Details
sr no. 9
Date: 15 July 2025
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

    def enqueue_from_rear(self, value):
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

    def enqueue_from_front(self, value):
        if self.length >= self.max_length:
            print("Queue is full")
            return None
        
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.length += 1
        print("Succesfully Inserted")

    def dequeue_from_front(self):
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


    def dequeue_from_rear(self):
        if self.length == 0:
            print(self.isEmpty())
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            while temp.next != self.last:
                temp = temp.next
            removed_node = self.last
            self.last = temp
            self.last.next = None
        self.length -= 1
        print(f"The value deleted is {removed_node.value}")

    def isEmpty(self):
        return "Queue is empty"

def input_restricted_queue(my_queue):
    print("INPUT RESTRICTED QUEUE".center(40, "-"))
    while True:
        try:
            print("\n")
            print("SUB MENU".center(24, "*"))
            print("1.Insert from rear")
            print("2.Delete from front")
            print("3.Delete from rear")
            print("4.Display")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    value = int(input("Enter a value: "))
                    my_queue.enqueue_from_rear(value)
                case 2:
                    my_queue.dequeue_from_front()
                case 3:
                    my_queue.dequeue_from_rear()
                case 4:
                    my_queue.print_queue()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)

def output_restricted_queue(my_queue):
    print("OUTPUT RESTRICTED QUEUE".center(40, "-"))
    while True:
        try:
            print("\n")
            print("SUB MENU".center(24, "*"))
            print("1.Insert from front")
            print("2.Insert from rear")
            print("3.Delete from front")
            print("4.Display")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    value = int(input("Enter a value: "))
                    my_queue.enqueue_from_front(value)
                case 2:
                    value = int(input("Enter a value: "))
                    my_queue.enqueue_from_rear(value)
                case 3:
                    my_queue.dequeue_from_front()
                case 4:
                    my_queue.print_queue()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)

def main():
    my_queue = None
    while True:
        try:
            print("\n")
            print("MAIN MENU".center(24, "*"))
            print("1.Create a queue")
            print("2.Input restricted queue")
            print("3.Output restricted queue")
            print("4.Display")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    value = int(input("Enter a value: "))
                    my_queue = Queue(value)
                case 2:
                    input_restricted_queue(my_queue)
                case 3:
                    output_restricted_queue(my_queue)
                case 4:
                    my_queue.print_queue()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()