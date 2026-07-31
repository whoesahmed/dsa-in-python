# DSA-in-Python

Python implementations of data structures and algorithms I've been working through while learning DSA. Nothing fancy — just clean, runnable code organized by topic.

Most files are standalone scripts. Clone the repo, run one, read the output. That's basically it.

## Setup

You'll need **Python 3.10+**. Everything here uses the standard library — no pip installs required.

```bash
git clone https://github.com/whoesahmed/dsa-in-python.git
cd dsa-in-python
```

If you like using a venv anyway:

```bash
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

(`requirements.txt` is empty on purpose — kept it there out of habit.)

## What's in here

**Algorithms**
- Binary search
- Merge sort & selection sort
- Square root via bisection
- Luhn algorithm (card number validation)
- Tower of Hanoi — this one's fun, it opens a turtle animation window

**Graphs & Trees**
- DFS on an adjacency matrix
- Dijkstra's shortest path
- N-Queens (backtracking)
- Adjacency list → matrix converter
- Valid parentheses generator (uses a BFS-style queue)

**Linear Data Structures**
- Hash table with chaining
- Singly linked list

Folder layout if you need it:

```
algorithms/
graphs-and-trees/
linear-data-structures/
```

## Running things

Pick a file and run it:

```bash
python algorithms/merge-sort/merge_algo.py
python graphs-and-trees/DFS.py
python graphs-and-trees/shortest-path-algorithm.py
python linear-data-structures/hash-table/linked_list.py
```

For the Hanoi visualizer, run it locally — it needs a display:

```bash
python algorithms/tower-of-hanoi/hanoi_solver.py
```

## Heads up

Some folder names don't perfectly match what's inside yet (yeah, `quicksort/quick_sort.py` is actually binary search right now). I'll clean that up over time. If you spot something off, feel free to open an issue or PR.

---

Built for learning. Take what's useful, ignore the rest.
