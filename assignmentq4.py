import erugraph as er
import upa
import compnetwork as comp
import project as proj
import random
import fast_targeted_order as fto
import targeted_order as to

compgraph = comp.load_graph("http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt")
p = float(3112)/float(906531)
ergraph =er.ERalg(1347,p)
m=3112/1347 
upagraph = upa.UPAgraph(1347,m)

erresiliences = proj.compute_resilience(ergraph, fto.fast_targeted_order(ergraph))
uparesiliences = proj.compute_resilience(upagraph, fto.fast_targeted_order(upagraph))
compresiliences = proj.compute_resilience(compgraph, fto.fast_targeted_order(compgraph))

import matplotlib.pyplot as plt
plt.plot(range(1347 + 1), erresiliences, label = 'ER Graph, p = %s' % round(p,5))
plt.plot(range(1347 + 1), uparesiliences, label = 'UPA Graph, m = %s' % m)
plt.plot(range(1347 + 1), compresiliences, label = 'Computer Graph')

#plt.xscale('log')
#plt.yscale('log')
plt.title("Line plot of ER, computer network and \n UPA graph's resiliencies as vertices get removed in targeted order")
plt.xlabel('Number of vertices removed')
plt.ylabel('Size (order) of largest component left')
plt.legend()
plt.show()    


    
    