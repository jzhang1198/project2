# write tests for bfs
import pytest
import networkx as nx
from search import graph

#@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    G = nx.DiGraph()  #generate a dummy graph for unit test
    G.add_nodes_from(['A','B','C','D','E','F','G'])
    G.add_edges_from([('A','B'), ('A','C'), ('B','D'),('B','E'),('C','F'),('C','G')])
        
    visited = G.bfs('A')
    
    assert visited[0] == 'A' #deterimine if the nodes were visited in the correct order
    assert visited[1] == 'B' or visited[1] == 'C'
    assert visited[2] == 'B' or visited[2] == 'C'
    
    assert len(G.nodes()) == len(visited) #check that all nodes were visited
    
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    
    G = nx.DiGraph()  #generate a dummy graph for unit test
    G.add_nodes_from(['A','B','C','D','E','F','G','H'])
    G.add_edges_from([('A','B'), ('A','C'), ('B','D'),('B','E'),('C','F'),('C','G')])
    
    test1 = G.bfs('A','G')
    test2 = G.bfs('A','H')
    
    assert test1 == ['A','C','G']
    assert test2 == None
    

test_bfs_traversal()

