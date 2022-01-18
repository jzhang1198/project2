import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        graph = self.graph #create graph
        
        adjacency_list = {} #generate an empty dictionary to become the adjacency list
        for n,nbrsdict in graph.adjacency(): #loop through the nodes and their neighbor dictionaries
            holder = []
            for neighbors in nbrsdict: #convert the neighbor dictionaries into lists
                holder.append(neighbors)
            adjacency_list[n] = holder #add node as the key and neighbors as the value into the dictionary
            
        queue = [] #generate queue, visited, and trajectory lists
        trajectories = []
        visited = []
    
        queue.append(start)
        trajectories.append([start])
        visited.append(start)
    
        while queue: 
            node = queue.pop(0) #pop current node and path 
            path = trajectories.pop(0) 
            
            if node == end: 
                return path
    
            for neighbor in adjacency_list[node]: #loop through the node neighbors
                if neighbor not in visited: 
                    new_path = list(path) 
                    new_path.append(neighbor)
                    trajectories.append(new_path) #append updated paths to trajectories
                    queue.append(neighbor) #update queue
                    visited.append(neighbor) #update visited
                    
        if end in graph.nodes():
            return None
        
        else:
            return visited #if no endpoint given, return visited 

    



