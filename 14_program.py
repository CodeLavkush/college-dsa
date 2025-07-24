"""
Practical Details
sr no. 14
Date: 24 July 2025
"""
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)

def main():
    my_list = []
    while True:
        try:
            n = int(input("Enter no. of elements: "))
            for i in range(n):
                element = int(input(f"Enter {i}th element: "))
                my_list.append(element)
            
            sorted_list = merge_sort(my_list)
            for i in sorted_list:
                print(i, end="\t")
            
            choice = input("\nDo you want continue? ")
            if choice.lower() == "no":
                break
            
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()