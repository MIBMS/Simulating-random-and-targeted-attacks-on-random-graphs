import upa
import fast_targeted_order as fto
import targeted_order as to
from time import time

FTOtimelist = {}
TOtimelist = {}

for n in range(10, 1000, 10):
    upagraph = upa.UPAgraph(n, 5)

    t0 = time()
    fto_order = fto.fast_targeted_order(upagraph)
    t1 = time()
    to_order = to.targeted_order(upagraph)
    t2 = time()
    
    FTOtimelist[n] = t1-t0
    TOtimelist[n] = t2-t1
    
import matplotlib.pyplot as plt
plt.plot(FTOtimelist.keys(), FTOtimelist.values(), 'bo', label = 'Fast Target Order Time')
plt.plot(TOtimelist.keys(), TOtimelist.values(), 'ro', label = 'Target Order Time')

#plt.xscale('log')
#plt.yscale('log')
plt.title("Point plot of running time of fast target order and \n target order implementations in Canopy Desktop Python")
plt.xlabel('Number of nodes in input graph')
plt.ylabel('Time')
plt.legend()
plt.show()    


    

    