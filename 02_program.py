"""
Practical Details
sr no. 2
Date: 20 June 2025
"""


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = arr[j]
    return arr

def create():
    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        element = int(input(f"Enter {i}th element: "))
        arr.append(element)
    return arr

def main():
    arr1 = []
    arr2 = []
    merged_arr = []
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Create 1st array")
            print("2.Create 2nd array")
            print("3.Sort 1st array")
            print("4.Sort 2nd array")
            print("5.Merge")
            print("6.Sorted merged array")
            print("7.Exit")
            choice = int(input("Enter your choice(1-7): "))
            match choice:
                case 1:
                    arr1 = create()
                    print("The 1st array is: ", arr1)
                case 2:
                    arr2 = create()
                    print("The 2nd array is: ", arr2)
                case 3:
                    arr1 = bubble_sort(arr1)
                    print("The sorted 1st array: ", arr1)
                case 4:
                    arr2 = bubble_sort(arr2)
                    print("The sorted 2nd array: ", arr2)
                case 5:
                    merged_arr = arr1 + arr2
                case 6:
                    print(merged_arr)
                case 7:
                    break
        except Exception as error:
            print("ERROR:", error)




if __name__ == "__main__":
    main()