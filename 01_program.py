"""
Practical Details
sr no. 1
Date: 19 June 2025
"""


def bubble_sort(arr):
    """
        first loop runs from last index.
        second loop runs from first index.
        comparing both elements and switch tham.
    """
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def main():
    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        element = int(input(f"Enter {i}th element: "))
        arr.append(element)
        
    while True:
        try:
            print("MAIN MENU".center(20, "*"))
            print("1.Display")
            print("2.Search")
            print("3.Sort")
            print("4.Reverse")
            print("5.Exit")
            choice = int(input("Enter your choice(1-5): "))
            match choice:
                case 1:
                    print(arr)
                case 2:
                    element = int(input("Enter value to be searched: "))
                    index = arr.index(element)
                    if index is not None:
                        print(f"Value found at location {index}")
                    else:
                        print("Value not found")
                case 3:
                    arr = bubble_sort(arr)
                case 4:
                    arr.reverse()
                case 5:
                    break
        except Exception as error:
            print("ERROR:", error)



if __name__ == "__main__":
    main()