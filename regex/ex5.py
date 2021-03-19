#Вам дана последовательность строк.
#Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)

import sys, re
pat = r'\b(.+)\1\b'
for line in sys.stdin:
  if re.search(pat, line):
    print(line.rstrip())
