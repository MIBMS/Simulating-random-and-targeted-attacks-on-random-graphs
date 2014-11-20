import erugraph as er
import upa
import compnetwork as comp
import project as proj
import random


#p is prob s.t. ER has approximately same number of edges as comp network with 
#|v| = 1347 |e| = 3112, we require p such that p * (1347 C 2) = 3112

p = float(3112)/float(906531)

ergraph =er.ERalg(1347,p)
#print proj.countedges(ergraph)

#m is the average degree of the computer network +
#though some edges are lost in upa trial

m=3112/1347 

upagraph = upa.UPAgraph(1347,m)
#print proj.countedges(upagraph)

compgraph = comp.load_graph("http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt")
#print proj.countedges(compgraph)
#print compgraph

def random_order(graph):
    '''
    Takes a graph and returns a list containing vertices in random order
    '''
    vertices = range(len(graph))
    random.shuffle(vertices)
    
    return vertices

erresiliences = proj.compute_resilience(ergraph, random_order(ergraph))
uparesiliences = proj.compute_resilience(upagraph, random_order(upagraph))
compresiliences = proj.compute_resilience(compgraph, random_order(compgraph))
    
import matplotlib.pyplot as plt
plt.plot(range(1347 + 1), erresiliences, label = 'ER Graph, p = %s' % round(p,5))
plt.plot(range(1347 + 1), uparesiliences, label = 'UPA Graph, m = %s' % m)
plt.plot(range(1347 + 1), compresiliences, label = 'Computer Graph')

#plt.xscale('log')
#plt.yscale('log')
plt.title("Line plot of ER, computer network and \n UPA graph's resiliencies as vertices get removed in random order")
plt.xlabel('Number of vertices removed')
plt.ylabel('Size (order) of largest component left')
plt.legend()
plt.show()    


    