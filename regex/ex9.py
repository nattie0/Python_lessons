'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz
Sample Output:

atraction
buz
'''

import re, sys

pat = r'(\w)\1+'
for line in sys.stdin:
  print(re.sub(pat, r'\1', line[:-1]))
