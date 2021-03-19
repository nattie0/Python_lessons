#Вам дана последовательность строк.
#В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки

import sys, re

pat = 'human'
p = 'computer'
for line in sys.stdin:
  print(re.sub(pat, p, line[:-1]))
