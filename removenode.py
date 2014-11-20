a = {0: set([1,2]), 1: set([0]), 2: set([])}
b = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
c = {0: set([1,4,5]), 1: set([2,6]), 2: set([7,3]), 3: set([7]), 4: set([1]), 5: set([2]), \
            6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,4,5,6,7,3])}
            
def remove(graph, node):
    graphcopy = graph.copy()
    for adjnode in graphcopy[node]:
        graphcopy[adjnode].discard(node)
    del graphcopy[node]
    return graphcopy
    
d = remove(a, 1)

