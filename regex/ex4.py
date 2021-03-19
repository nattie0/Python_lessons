#Вам дана последовательность строк.
#Выведите строки, содержащие обратный слеш "\"

import sys, re
pat = '\\'
for line in sys.stdin:
    if pat in line:
        print(line.rstrip())
