"""
Practical Details
sr no. 12
Date: 24 July 2025
"""
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            j -= 1
    return my_list

def main():
    my_list = []
    while True:
        try:
            n = int(input("Enter no. of elements: "))
            for i in range(n):
                element = int(input(f"Enter {i}th element: "))
                my_list.append(element)
            
            sorted_list = insertion_sort(my_list)
            for i in sorted_list:
                print(i, end="\t")
            
            choice = input("\nDo you want continue? ")
            if choice.lower() == "no":
                break
            
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()