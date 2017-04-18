import sys
import multiprocessing as mp

print("Python version %s " % str(sys.version))
print("cores %s " % str(mp.cpu_count()))

if True:
  print("tady")
else:
  print("Tady ne")
  a = 0
  b = 1
  c = b /a
  
  
