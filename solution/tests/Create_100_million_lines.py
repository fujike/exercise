# coding: shift-JIS

import time
import os
import sys
import random

t1 = time.time()

print('\n Start ... \n')

os.chdir(sys.path[0])

outfile = 'line_100_million.txt'

out = open(outfile, 'w')

for i in range(1, 100000000 + 1):
  id = str(i).zfill(9)
  v = random.randint(1, 999)
  out.write('%s %d\n' % (id, v))

out.close()

print('\n 処理時間: %.1f 秒' % (time.time() - t1))
print('\n End. \n')
