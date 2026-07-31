# DSA in Python

Python implementations of core data structures and algorithms, built while working through a structured DSA curriculum. Organized by topic — each file is a focused, standalone implementation with its time/space complexity noted.

## Structure

**Algorithms**

| File | Complexity |
|---|---|
| `binary-search/binary_search_algo.py` | O(log n) |
| `bisection-sort/bisection.py` | O(log n) — bisection method |
| `luhn-algorithm/luhn.py` | O(n) — card validation |
| `merge-sort/merge_algo.py` | O(n log n) time, O(n) space |
| `quicksort/quick_sort.py` | O(n log n) avg, O(n²) worst |
| `selection-sort/selection_sort.py` | O(n²) |
| `tower-of-hanoi/hanoi_solver.py` | O(2ⁿ) |

**Graphs & Trees**

| File | Complexity |
|---|---|
| `adjacency-list-to-matrix.py` | O(V²) |
| `BFS.py` | O(V + E) |
| `DFS.py` | O(V + E) |
| `n-queens-algorithm.py` | O(N!) — backtracking |
| `shortest-path-algorithm.py` | O((V + E) log V) — Dijkstra |

**Dynamic Programming**

| File | Complexity |
|---|---|
| `fibonacci_series.py` | O(n) time, O(1) space — bottom-up |

**Linear Data Structures**

| File | Complexity |
|---|---|
| `hash-table/hash-table.py` | O(1) average — add / lookup / remove |
| `hash-table/linked_list.py` | O(n) — add / remove, singly linked |

## Setup

Requires Python 3.10+. Standard library only — no external dependencies.

```bash
git clone https://github.com/whoesahmed/dsa-in-python.git
cd dsa-in-python
```

## Running

Each file runs standalone:

```bash
python algorithms/binary-search/binary_search_algo.py
python algorithms/merge-sort/merge_algo.py
python graphs-and-trees/shortest-path-algorithm.py
python linear-data-structures/hash-table/hash-table.py
```

Tower of Hanoi opens a Turtle graphics window — run locally, not headless:

```bash
python algorithms/tower-of-hanoi/hanoi_solver.py
```

## Notes

## Notes

Built as part of an ongoing DSA learning path. Code favors clarity over premature optimization — each implementation is meant to demonstrate the underlying concept, not compete with the standard library.

Quicksort uses in-place partitioning (last-element pivot) — worth noting this degrades to O(n²) on already-sorted input; randomized pivot selection would fix that but wasn't needed for this exercise.

---

Feedback and PRs welcome.
