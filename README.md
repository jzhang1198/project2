![BuildStatus](https://github.com/jzhang1198/Project2/workflows/Project2/badge.svg?event=push)

# Project 2
Breadth-first search

# Description
Within this repository is an implementation of a breadth-first search algorithm, installable as a Python module. The breadth-first search function within graph.py is contained within a Graph class. To use this function, first instantiate a Graph object by providing the path of an adjacency list file as an attribute. Then, the breadth-first search algorithm can be applied to this object by calling the bfs function. bfs takes in two arguments: a start node and an end node, the later being optional. Depending on the input arguments and the graph structure, the three possible outputs are a list containing the shortest path between the start and end node (if end node is provided), a list of all nodes in order of traversal (if no end node is provided), or None (if no path exists between start and end node). 
