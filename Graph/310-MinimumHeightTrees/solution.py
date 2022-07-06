from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        adjacency_list = [set() for _ in range(n)]
        for start, end in edges:
            adjacency_list[start].add(end)
            adjacency_list[end].add(start)

        leaves = []
        for index, neighbors in enumerate(adjacency_list):
            if len(neighbors) == 1:
                leaves.append(index)

        leaf_reamining = n
        while leaf_reamining > 2:
            new_leaves = []
            leaf_reamining -= len(leaves)
            for _ in range(len(leaves)):
                leaf_node = leaves.pop()
                neighbor = adjacency_list[leaf_node].pop()
                adjacency_list[neighbor].remove(leaf_node)
                if len(adjacency_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves
