#Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.

n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for j in range(n)]
res = [[matrix[i][j] for i in range(n)] for j in range(m)]
for i in res:
  print(*i)
