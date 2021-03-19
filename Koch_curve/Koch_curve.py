n = int(input())
a = 'aba'
line = ''
nline = ''
for i in range(n):
    if line:
        for j in line:
            nline += a + j 
            line, nline = nline, ''
            line += a
    else:
        line = 'aba'
d = {'a': 'turn 60', 'b': 'turn -120'}
for i in line:
    print(d[i])
