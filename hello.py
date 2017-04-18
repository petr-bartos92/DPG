import sys
import multiprocessing as mp

print("Python version %s " % str(sys.version))
print("cores %s " % str(mp.cpu_count()))

