import numpy as np
import sys
import os
def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

def memory_usage_resource():
    import resource
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem

mem_resource = []
mem_psutil = []
for i in range(1, 21):
    a = np.zeros((1000 * i, 100 * i))
    mem_resource.append(memory_usage_resource())
    mem_psutil.append(memory_usage_psutil())

#import psutil
#process = psutil.Process(2324)
#mem = process.memory_info()[0]/float(2**20)
#print(mem)
#import os
#cmd = "ps aux | grep -i hello"
#a = os.system()


