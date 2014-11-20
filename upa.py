import upatrial as upa
import itertools

def make_complete_graph(num_nodes):
    '''Takes the number of nodes num_nodes and returns a dictionary corresponding 
    to a complete undirected graph with the specified number of nodes. A complete graph 
    contains all possible edges subject to the restriction that self-loops are not allowed.
    The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive.
    Otherwise, the function returns a dictionary corresponding to the empty graph. '''
    
    def findsubsets(S,m):
        '''finds all subsets of size m of S'''
        return set(itertools.combinations(S, m))
        
    if num_nodes > 0:
        vset = set(range(num_nodes))
        graph = {}
        for vertex in vset:
            graph[vertex] = set()                
        for pairtuple in findsubsets(vset, 2):
            elt1 = pairtuple[0]
            elt2 = pairtuple[1]
            if elt1 != elt2:
                graph[elt1].add(elt2)
                graph[elt2].add(elt1) 
        
        return graph
    
    else:
        return {}
        
def UPAgraph(n, m):
    '''Creates a UPA graph with n vertices and initialized with a complete
    graph on m vertices'''
    graph = make_complete_graph(m)
    #creates a UPA simulator using UPATrial class, which updates itself 
    #UPATrial class is called once, then each call of run_trial will
    #update the sample space V from which the m nodes are chosen. V is initialized
    #to range(m)
    UPAsim = upa.UPATrial(m)
    for i in range(m, n): 
        graph[i] = set()        
    for i in range(m, n):        
        #adjvset is V' which is set of vertices adjacent to i
        adjvset = UPAsim.run_trial(m)
        for adj_node in adjvset:
            graph[i].add(adj_node)
            graph[adj_node].add(i)
    return graph

    