"""
Practical Details
Name: Program to implement quadratic probing in hash table
sr no. 20
Date: 14 Aug 2025
"""
class HashTableQuadratic:
    def __init__(self, size=7):
        self.size = size
        self.data_map = [None] * size

    def __hash(self, value):
        return hash(str(value)) % self.size

    def insert(self, value):
        index = self.__hash(value)
        i = 1
        while self.data_map[index] is not None and self.data_map[index] != value:
            index = (index + i * i) % self.size
            i += 1
            if i > self.size:
                print("HashTable is full!")
                return
        self.data_map[index] = value

    def search(self, value):
        index = self.__hash(value)
        i = 1
        while self.data_map[index] is not None:
            if self.data_map[index] == value:
                print(f"Value {value} found at index {index}")
                return
            index = (index + i * i) % self.size
            i += 1
            if i > self.size:
                break
        print(f"Value {value} not found")

    def delete(self, value):
        index = self.__hash(value)
        i = 1
        while self.data_map[index] is not None:
            if self.data_map[index] == value:
                self.data_map[index] = None
                print(f"Deleted value: {value}")
                return
            index = (index + i * i) % self.size
            i += 1
            if i > self.size:
                break
        print(f"Value {value} not found for deletion")

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


def main():
    ht = HashTableQuadratic()
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Insert")
            print("2.Search")
            print("3.Delete")
            print("4.Print")
            print("5.Quit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    n = int(input("Enter no. of elements: "))
                    for _ in range(n):
                        value = input("Enter value: ")
                        ht.insert(value)
                    print("Values inserted")
                case 2:
                    key = input("Enter value to search: ")
                    ht.search(key)
                case 3:
                    key = input("Enter value to delete: ")
                    ht.delete(key)
                case 4:
                    ht.print_table()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()