# Course Schedule

Problem can be found in [here](https://leetcode.com/problems/course-schedule)!

### [Solution](/Graph/207-CourseSchedule/solution.py): Depth-First Search

```python
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Construct edges for DFS
    edges = defaultdict(list)
    for dest, src in prerequisites:
        edges[src].append(dest)

    stack = []
    node_status = [0] * numCourses          # 0: White (Not Discovered Yet), 1: Gray (Being Explored), 2: Black (Explored)
    for vertex in range(numCourses):
        stack.append(vertex)
        while stack:
            node = stack[-1]

            # The node has not been visited yet
            if node_status[node] == 0:
                node_status[node] = 1
                for neighbor in edges[node]:
                    if node_status[neighbor] == 0:
                        stack.append(neighbor)

                    # If we find a gray node, meaning that we have visited this node twice i.e. we find a cycle!
                    elif node_status[neighbor] == 1:
                        return False
                    else:
                        continue

            # In either cases, this means that we have fully explored the node. So, just simply pop the node out.
            else:
                node_status[node] = 2
                stack.pop()

    return True
```

Explanation: By performing a DFS, we can determine whether this graph is a DAG (Directed Acyclic Graph) or not. If so, we can finish all courese (should return True).

Time Complexity: ![O(V + E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V + E)>), Space Complexity: ![O(V + E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V + E)>), where V is the total number of courses and E is the total number of prerequisites.
