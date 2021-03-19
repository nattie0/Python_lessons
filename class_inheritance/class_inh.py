def isparent(a, b):
    if b in base or a == b:
        if a == b or a in base[b]:
            return True
        elif base[b]:
            for i in base[b]:
                if isparent(a, i):
                    return isparent(a, i)
        else: return False
    else: return False
  
base = {}
n = int(input())
for i in range(n):
    a = input()
    if ':' in a:
        a, b = a.split(' : ')
        base[a] = b.split()
    else: base[i] = None
q = int(input())
for i in range(q):
    if isparent(*input().split()):
        print('Yes')
    else: print('No')
