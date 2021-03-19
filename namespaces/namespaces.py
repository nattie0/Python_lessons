def create(a, b):
    dic[a] = {'parent':b, 'vars' : set()}
    return ''
  
def add(a, b):
    dic[a]['vars'].add(b)
    return ''
  
def get(a, b):
    if b in dic[a]['vars']:
        print(a)
    elif dic[a].get('parent'):
        get(dic[a]['parent'], b)
    else: print(None)
    
  d = {'create': create, 'add': add, 'get': get}
  n = int(input())
  dic = {'global': {'vars': set()}}
  for i in range(n):
      fun, a, b = input().split()
      d[fun](a, b)
