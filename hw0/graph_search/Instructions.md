# Graph Search

## Problem Description
Indicate the order in which nodes are visited in breadth-first and depth-first searches of undirected graphs. Graphs will be given in text format as an adjacency
list, with nodes represented by letters. For example,

```
a: b, c, d

b: a, d

c: a

d: a, b

e: f

f: e
```

To break ties between neighbors of a single node, assume the first visited is in alphabetical order. If the graph is not connected, then give the traversal order of the connected component containing the node a. In this example, a BFS starting at node a would visit the nodes in order a, b, c, d, (leaving e and f unvisited, since they are in a different connected component than a) and a DFS would visit them in order a, b, d, c. To indicate this, upload a text file that has these orders on two lines (BFS order on line 1 and DFS order on line 2), with nodes separated by spaces on a line. For example:

```
a b c d

a b d c
```

## Code Instructions

1. Enter the `graph_search` folder:
```bash
cd hw0/graph_search
```

2. Modify `input_graph.txt` file to your own input, in the format same to the Problem Description.
3. Run `graph_search.py`:
```bash
python graph_search.py
```

The script will both generate `output.txt` file and print the results in the terminal.