"""
    This class represents a disjoint set data structure. It uses the union-find algorithm to manage a set.

    Rank:
    Roughly represents the depth (or height) of teh tree representing a set. 
    Initially, each set has a rank of 1. (Each set is just one element).
"""
class DisjointSet:
    def __init__(self, num_elements):
        self.parent = list(range(num_elements)) #tracks the "parent" of each element where initially each element is its own set
        self.rank = [0] * num_elements #list is used to optimize the union operation 
    
    def find(self, x):
        """Find the root of the set that x belongs to."""

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        
        return self.parent[x]
    
    def union(self, x, y):
        """
        Merge the sets that x and y belong to.

        This technique helps to keep the trees flat by always attaching the 
        shorter tree under the root of the taller tree, minimizing the depth and 
        speeding up future operations.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


"""

Why This Data Structure Is Useful:
    Efficient for Kruskal's algorithm: 
        Union-Find allows efficient union and find operations, which are essential for checking if two cells are 
        in the same set or not (in your maze generation). It ensures that the union and find operations are fast,
        even after many operations.
    Path compression: 
        This optimization ensures that future calls to find are faster, 
        as it reduces the height of the trees by making all nodes point directly to the root 
        after each find operation.
    Union by rank: 
        This keeps the trees balanced by always attaching the smaller tree to 
        the larger tree, preventing the formation of deep trees.

"""