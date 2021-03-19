#Вам дана последовательность строк.
#Выведите строки, содержащие "cat" в качестве слова.

import sys, re

pat = r'\b(cat)\b'
for line in sys.stdin:
  line = line.rstrip()
  if re.search(pat, line):
    print(line)
