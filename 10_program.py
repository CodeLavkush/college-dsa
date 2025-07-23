"""
Practical Details
sr no. 10
Date: 17 July 2025
"""


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def main():
    my_list = []
    while True:
        try:
            n = int(input("Enter no. of elements: "))
            for i in range(n):
                element = int(input(f"Enter {i}th element: "))
                my_list.append(element)
            
            sorted_list = bubble_sort(my_list)
            for i in sorted_list:
                print(i, end="\t")
            
            choice = input("\nDo you want continue? ")
            if choice.lower() == "no":
                break
            
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()