"""
Practical Details
Name: Program to create a binary tree and 
traversing tree using postorder, preorder, inorder.
sr no. 15
Date: 25 July 2025
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True 
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def dfs_preorder(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    def dfs_postorder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    def dfs_inorder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
def display(my_tree):
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Pre-Order")
            print("2.In-order")
            print("3.Post-Order")
            print("4.Exit")
            choice = int(input("Enter your choice(1-4): "))
            match choice:
                case 1:
                    print("The Pre-Order Traversal is: ", *my_tree.dfs_preorder())
                case 2:
                    print("The In-Order Traversal is: ", *my_tree.dfs_inorder())
                case 3:
                    print("The Post-Order Traversal is: ", *my_tree.dfs_postorder())
                case 4:
                    break
        except Exception as error:
            print("ERROR:", error)

def main():
    my_tree = BinarySearchTree()
    while True:
        try:
            print("MAIN MENU".center(24, "*"))
            print("1.Create a binary search tree")
            print("2.Display the tree")
            print("3.Exit")
            choice = int(input("Enter your choice(1-3): "))
            match choice:
                case 1:
                    while True:
                        value = int(input("Enter a value or -1 to exit: "))
                        if value == -1:
                            print("Succesfully created")
                            break
                        my_tree.insert(value)
                case 2:
                    display(my_tree)
                case 3:
                    break
        except Exception as error:
            print("ERROR:", error)


if __name__ == "__main__":
    main()