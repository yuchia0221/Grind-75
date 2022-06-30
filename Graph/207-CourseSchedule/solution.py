from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for dest, src in prerequisites:
            edges[src].append(dest)

        stack = []
        node_status = [0] * numCourses
        for vertex in range(numCourses):
            stack.append(vertex)
            while stack:
                node = stack[-1]
                if node_status[node] == 0:
                    node_status[node] = 1
                    for neighbor in edges[node]:
                        if node_status[neighbor] == 0:
                            stack.append(neighbor)
                        elif node_status[neighbor] == 1:
                            return False
                        else:
                            continue
                else:
                    node_status[node] = 2
                    stack.pop()

        return True
