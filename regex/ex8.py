#Вам дана последовательность строк.
#В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.

import re, sys

pat = r'\b\w{2,}\b'
res = 'argh'
for line in sys.stdin:
  t = re.findall(pat, line)
  for i in t:
    line = re.sub(r'\b'+i+r'\b', i[1]+i[0]+i[2:], line)
  print(line[:-1])
