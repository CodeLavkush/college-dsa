"""
Practical Details
Name: Program to search element using binary search
sr no. 21
Date: 25 july 2025
"""
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def binary_search(my_list, target):
    sorted_list = bubble_sort(my_list)
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def main():
    my_list = []
    while True:
        try:
            print("MAIN MENU".center(30, "*"))
            print("1.Create a list")
            print("2.Search")
            print("3.Display")
            print("4.Exit")
            choice = int(input("Enter your choice(1-4): "))
            match choice:
                case 1:
                    n = int(input("Enter no. of elements: "))
                    for i in range(n):
                        element = int(input(f"Enter {i}th element: "))
                        my_list.append(element)
                case 2:
                    element = int(input("Enter element to search: "))
                    index = binary_search(my_list, element)
                    if index is not None:
                        print(f"The value is at {index} index")
                    else:
                        print("The value not found.")
                case 3:
                    print(*my_list)
                case 4:
                    break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()
