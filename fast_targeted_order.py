def compute_degree(graph, node):
    '''
    computes degree of node in graph
    '''
    return len(graph[node])

def fast_targeted_order(graph):
    '''
    Computes a list of nodes in graph in decreasing order of degrees
    '''
    graphcopy = {}
    for node in graph:
        graphcopy[node] = set(graph[node])
    degreesets = []
    for degree in range(len(graphcopy)):
        degreesets.append(set())
    for node in range(len(graphcopy)):
        degreesets[compute_degree(graphcopy,node)].add(node)
    targeted_order = []
    for degree in range(len(graphcopy)-1, -1, -1):
        while degreesets[degree] != set():
            random_maxdnode = degreesets[degree].pop()
            for neighbor in graphcopy[random_maxdnode]:
                degreeneighbor = len(graphcopy[neighbor])
                degreesets[degreeneighbor].remove(neighbor)
                degreesets[degreeneighbor - 1].add(neighbor)
                graphcopy[neighbor].remove(random_maxdnode)
            targeted_order.append(random_maxdnode)
            del graphcopy[random_maxdnode]
          
    return targeted_order

        