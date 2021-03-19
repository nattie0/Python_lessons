#Вам дана последовательность строк.
#Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

import sys, re
pat = 'z...z'
for line in sys.stdin:
    if re.search(pat, line):
        print(line.rstrip())
