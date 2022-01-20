# write tests for bfs
import pytest
import networkx as nx
from search import graph

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
     
    try: #if running on local device, instantiate a Graph object using the following path
        file = '../data/dummy_network.adjlist'
        dummy = graph.Graph(file)  
    
    except: #if running on GitHub actions, instantiate a Graph object using the following path
        file = 'data/dummy_network.adjlist' 
        dummy = graph.Graph(file) 
        
        
    visited = dummy.bfs('A') #traverse the graph 
    
    assert visited[0] == 'A' #deterimine if the nodes were visited in the correct order
    assert visited[1] == 'B' or visited[1] == 'C'
    assert visited[2] == 'B' or visited[2] == 'C'
    assert len(dummy.graph.nodes()) - 1 == len(visited) #check that all nodes were visited (note that node H is not connected and won't be traversed)
    
    
@pytest.fixture
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
    
    try: #if running on local device, instantiate a Graph object using the following path
        file = '../data/dummy_network.adjlist'
        dummy = graph.Graph(file)  
    
    except: #if running on GitHub actions, instantiate a Graph object using the following path
        file = 'data/dummy_network.adjlist' 
        dummy = graph.Graph(file) 
    
    test1 = dummy.bfs('A','G')
    test2 = dummy.bfs('A','H')
    
    assert test1 == ['A','C','G']
    assert test2 == None

