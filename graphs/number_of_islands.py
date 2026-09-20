"""LeetCode #200: Number of Islands (Medium)"""
from typing import List

def num_islands(grid: List[List[str]]) -> int:
    """Count number of islands in a 2D grid.
    Time Complexity: O(M * N)
    Space Complexity: O(M * N) recursion stack
    """
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count

def test_num_islands():
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    assert num_islands(grid) == 1
