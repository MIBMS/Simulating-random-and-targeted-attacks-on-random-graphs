'''bfs_visited, '''

from collections import deque as que

def bfs_visited(ugraph, start_node):
    '''
    Takes the undirected graph ugraph and the node start_node and 
    returns the set consisting of all nodes that are visited by a 
    breadth-first search that starts at start_node
    '''
    queue = que()
    visited = set([start_node])
    queue.append(start_node)
    while queue != que():
        firstnode = queue.popleft()
        for neighbor in ugraph[firstnode]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    '''
    Takes the undirected graph ugraph and returns a list of sets, where 
    each set consists of all the nodes (and nothing else) in a connected 
    component, and there is exactly one set in the list for each connected 
    component in ugraph and nothing else.
    '''
    remainingnodes = set(ugraph.keys())
    components = []
    while remainingnodes != set():
        sourcenode = remainingnodes.pop()
        visited = bfs_visited(ugraph, sourcenode)
        components.append(visited)
        for node in visited:
            remainingnodes.discard(node)
    return components

def largest_cc_size(ugraph):
    '''
    Takes the undirected graph ugraph and returns the size (an integer) of the 
    largest connected component in ugraph
    '''
    components = cc_visited(ugraph)
    componentsize = []
    for component in components:
        componentsize.append(len(component))
    componentsize = sorted(componentsize)
    if len(componentsize) == 0:
        return 0
    else:
        return componentsize[-1]
    
#GRAPH0 = {0: set([1,4,5]), 1: set([2,6]), 2: set([7,3]), 3: set([7]), 4: set([1]), 5: set([2]), \
#            6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,4,5,6,7,3])}
#a = largest_cc_size(GRAPH0)

def countedges(graph):
    count = 0
    for i in graph:
        count += len(graph[i])
    return count/2

def remove(graph, node):
    '''removes node from graph'''
    graphcopy = graph.copy()
    for adjnode in graphcopy[node]:
        graphcopy[adjnode].discard(node)
    del graphcopy[node]
    return graphcopy

def compute_resilience(ugraph, attack_order):
    '''Takes the undirected graph ugraph, a list of nodes attack_order and 
    iterates through the nodes in attack_order. For each node in the list, 
    the function removes the given node and its edges from the graph and then 
    computes the size of the largest connected component for the resulting graph.
    '''
    ccsizeslist = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph = remove(ugraph,node)
        ccsizeslist.append(largest_cc_size(ugraph))
    return ccsizeslist
        
             