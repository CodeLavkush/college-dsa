"""
Practical Details
Name: Prgram to generate the adjacency matrix.
sr no. 18
Date: 31 July 2025
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        vertices = list(self.adj_list.keys())
        for v1 in vertices:
            for v2 in vertices:
                if v2 in self.adj_list[v1]:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
    
    def add_vertax(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

def main():
    my_graph = Graph()
    while True:
        try:
            n = int(input("Enter no. of vertices: "))
            for i in range(n):
                my_graph.add_vertax(i + 1)
            print("Enter edge pair<V1><V2>")
            print("Enter -1 -1 to exit: ")
            while True:
                v1, v2 = map(int, input("Enter Pair: ").split())
                my_graph.add_edge(v1, v2)
                if v1 == -1 and v2 == -1:
                    my_graph.print_graph()
                    break
            break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()