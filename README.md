# 🧩 LeetCode Solutions in Python

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Solutions-FFA116?logo=leetcode&logoColor=black)](https://leetcode.com)

Production-grade Python 3 implementations for curated LeetCode problems (Easy, Medium, Hard), complete with docstrings, typing hints, approach explanations, unit tests (`pytest`), and optimal **Time & Space Complexity analysis**.

---

## 📊 Summary Table

| # | Problem | Category | Difficulty | Time Complexity | Space Complexity | Solution |
|---|---|---|---|---|---|---|
| 1 | Two Sum | Array & Hash Table | 🟢 Easy | $O(N)$ | $O(N)$ | [two_sum.py](arrays/two_sum.py) |
| 121 | Best Time to Buy & Sell Stock | Array | 🟢 Easy | $O(N)$ | $O(1)$ | [best_time_stock.py](arrays/best_time_to_buy_sell_stock.py) |
| 238 | Product of Array Except Self | Array | 🟡 Medium | $O(N)$ | $O(1)$ | [product_except_self.py](arrays/product_of_array_except_self.py) |
| 53 | Maximum Subarray (Kadane) | Dynamic Programming | 🟢 Easy | $O(N)$ | $O(1)$ | [maximum_subarray.py](arrays/maximum_subarray.py) |
| 153 | Find Min in Rotated Sorted Array | Binary Search | 🟡 Medium | $O(\log N)$ | $O(1)$ | [find_min_rotated.py](arrays/find_minimum_in_rotated_sorted_array.py) |
| 11 | Container With Most Water | Two Pointers | 🟡 Medium | $O(N)$ | $O(1)$ | [container_water.py](arrays/container_with_most_water.py) |
| 242 | Valid Anagram | Hash Table | 🟢 Easy | $O(N)$ | $O(1)$ | [valid_anagram.py](strings/valid_anagram.py) |
| 125 | Valid Palindrome | Two Pointers | 🟢 Easy | $O(N)$ | $O(1)$ | [valid_palindrome.py](strings/valid_palindrome.py) |
| 3 | Longest Substring Without Repeating | Sliding Window | 🟡 Medium | $O(N)$ | $O(\min(N, M))$ | [longest_substring.py](strings/longest_substring_without_repeating_characters.py) |
| 5 | Longest Palindromic Substring | Dynamic Programming | 🟡 Medium | $O(N^2)$ | $O(1)$ | [longest_palindrome.py](strings/longest_palindromic_substring.py) |
| 76 | Minimum Window Substring | Sliding Window | 🔴 Hard | $O(N)$ | $O(K)$ | [min_window.py](sliding_window/minimum_window_substring.py) |
| 20 | Valid Parentheses | Stack | 🟢 Easy | $O(N)$ | $O(N)$ | [valid_parentheses.py](stack/valid_parentheses.py) |
| 33 | Search in Rotated Sorted Array | Binary Search | 🟡 Medium | $O(\log N)$ | $O(1)$ | [search_rotated.py](binary_search/search_in_rotated_sorted_array.py) |
| 206 | Reverse Linked List | Linked List | 🟢 Easy | $O(N)$ | $O(1)$ | [reverse_linked_list.py](linked_list/reverse_linked_list.py) |
| 21 | Merge Two Sorted Lists | Linked List | 🟢 Easy | $O(N + M)$ | $O(1)$ | [merge_sorted_lists.py](linked_list/merge_two_sorted_lists.py) |
| 141 | Linked List Cycle (Floyd) | Two Pointers | 🟢 Easy | $O(N)$ | $O(1)$ | [linked_list_cycle.py](linked_list/linked_list_cycle.py) |
| 104 | Maximum Depth of Binary Tree | Tree (DFS) | 🟢 Easy | $O(N)$ | $O(H)$ | [max_depth_tree.py](trees/maximum_depth_of_binary_tree.py) |
| 226 | Invert Binary Tree | Tree | 🟢 Easy | $O(N)$ | $O(H)$ | [invert_binary_tree.py](trees/invert_binary_tree.py) |
| 100 | Same Tree | Tree (DFS) | 🟢 Easy | $O(N)$ | $O(H)$ | [same_tree.py](trees/same_tree.py) |
| 236 | Lowest Common Ancestor of Binary Tree | Tree (DFS) | 🟡 Medium | $O(N)$ | $O(H)$ | [lca_tree.py](trees/lowest_common_ancestor.py) |
| 200 | Number of Islands | Graph (BFS/DFS) | 🟡 Medium | $O(M \times N)$ | $O(M \times N)$ | [number_of_islands.py](graphs/number_of_islands.py) |
| 207 | Course Schedule (Kahn Algo) | Graph (Topological) | 🟡 Medium | $O(V + E)$ | $O(V + E)$ | [course_schedule.py](graphs/course_schedule.py) |
| 70 | Climbing Stairs | Dynamic Programming | 🟢 Easy | $O(N)$ | $O(1)$ | [climbing_stairs.py](dp/climbing_stairs.py) |
| 322 | Coin Change | Dynamic Programming | 🟡 Medium | $O(N \times \text{amount})$ | $O(\text{amount})$ | [coin_change.py](dp/coin_change.py) |
| 300 | Longest Increasing Subsequence | Dynamic Programming | 🟡 Medium | $O(N \log N)$ | $O(N)$ | [lis.py](dp/longest_increasing_subsequence.py) |

---

## 🛠️ Testing

All solutions include inline unit test suits using `pytest`.

To run tests across all solutions:
```bash
pip install pytest
pytest
```
