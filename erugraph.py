import itertools
import random

def ERalg(n, p):
    '''ER algorithm takes n and p and produces an undirected graph with n vertices.
    Each possible edge (nC2 of them) is considered and added to edge set with
    probability 0<=p<=1'''
    
    vset = set(range(n))
    graph = {}
    for vertex in vset:
        graph[vertex] = set()
    
    def findsubsets(S,m):
        '''finds all subsets of cardinality m of S'''
        return set(itertools.combinations(S, m))
        
    for pairtuple in findsubsets(vset, 2):
        elt1 = pairtuple[0]
        elt2 = pairtuple[1]
        if elt1 != elt2:
            randomnumber = random.random()
            if randomnumber < p:
                graph[elt1].add(elt2)
                graph[elt2].add(elt1)  
                

                
    return graph