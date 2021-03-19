'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.
'''

string = input()
pat = input()
number = 0
index = 0
while pat in string[index:]:
  index += 1 + s[index:].index(pat)
  number += 1
print(number)
