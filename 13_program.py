"""
Practical Details
sr no. 13
Date: 24 July 2025
"""
def main():
    my_list = []
    while True:
        try:
            print("\n")
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
                    searched_value = my_list.index(element)
                    print(f"The value is at {searched_value}")
                case 3:
                    for i in my_list:
                        print(i, end="\t")
                case 4:
                    break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()