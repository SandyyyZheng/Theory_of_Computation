#!/usr/bin/env python3
"""
Graph Search Script
Performs BFS and DFS on an undirected graph starting from node 'a'.
"""

from collections import deque
import os


def parse_graph(lines):
    """
    Parse adjacency list format into a graph dictionary.

    Args:
        lines: List of strings in format "node: neighbor1,neighbor2,..."

    Returns:
        Dictionary mapping each node to a sorted list of neighbors
    """
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Split on colon
        parts = line.split(':')
        if len(parts) != 2:
            continue

        node = parts[0].strip()
        neighbors_str = parts[1].strip()

        # Parse neighbors
        if neighbors_str:
            neighbors = [n.strip() for n in neighbors_str.split(',')]
            # Sort neighbors alphabetically for tie-breaking
            graph[node] = sorted(neighbors)
        else:
            graph[node] = []

    return graph


def bfs(graph, start):
    """
    Perform breadth-first search starting from the given node.

    Args:
        graph: Dictionary representing the adjacency list
        start: Starting node

    Returns:
        List of nodes in the order they were visited
    """
    if start not in graph:
        return []

    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        # Add neighbors in alphabetical order (already sorted in graph)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order


def dfs(graph, start):
    """
    Perform depth-first search starting from the given node.

    Args:
        graph: Dictionary representing the adjacency list
        start: Starting node

    Returns:
        List of nodes in the order they were visited
    """
    if start not in graph:
        return []

    visited = set()
    order = []

    def dfs_helper(node):
        if node in visited:
            return

        visited.add(node)
        order.append(node)

        # Visit neighbors in alphabetical order (already sorted in graph)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

    dfs_helper(start)
    return order


def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Read input from input_graph.txt in the same directory
    input_file = os.path.join(script_dir, 'input_graph.txt')
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Parse the graph
    graph = parse_graph(lines)

    # Perform BFS and DFS starting from node 'a'
    bfs_order = bfs(graph, 'a')
    dfs_order = dfs(graph, 'a')

    # Prepare output
    bfs_line = ' '.join(bfs_order)
    dfs_line = ' '.join(dfs_order)

    # Output to console
    print(bfs_line)
    print(dfs_line)

    # Write to output.txt in the same directory
    output_file = os.path.join(script_dir, 'output.txt')
    with open(output_file, 'w') as f:
        f.write(bfs_line + '\n')
        f.write(dfs_line + '\n')

    print(f"\n结果已保存到: {output_file}")


if __name__ == '__main__':
    main()
