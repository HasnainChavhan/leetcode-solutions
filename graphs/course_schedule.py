"""LeetCode #207: Course Schedule (Medium / Topological Sort Kahn's Algo)"""
from typing import List
from collections import deque

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Determine if you can finish all courses given prerequisites.
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    adj = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return visited == num_courses

def test_can_finish():
    assert can_finish(2, [[1, 0]]) == True
    assert can_finish(2, [[1, 0], [0, 1]]) == False
