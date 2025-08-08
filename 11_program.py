"""
Practical Details
Name: Program to implement selection sort.
sr no. 11
Date: 17 July 2025
"""

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def main():
    my_list = []
    while True:
        try:
            n = int(input("Enter no. of elements: "))
            for i in range(n):
                element = int(input(f"Enter {i}th element: "))
                my_list.append(element)
            
            sorted_list = selection_sort(my_list)
            for i in sorted_list:
                print(i, end="\t")
            
            choice = input("\nDo you want continue? ")
            if choice.lower() == "no":
                break
            
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()