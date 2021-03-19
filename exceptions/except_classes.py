def wasparent(exc):
  if base.get(exc):
    for parent in base[exc]:
      if parent in log:
        return True
      elif wasparent(parent):
        return True
    else: return False
  else: return False
      
base = {}
log = []
cl = set()
n = int(input())
for i in range(n):
  a = input()
  if ':' in a:
    a, b = a.split(' : ')
    b = b.split()
  else: b = None
  base[a] = b
q = int(input())
for i in range(q):
  exc = input()
  if exc not in cl:
    if exc in log or wasparent(exc):
      cl.add(exc)
      print(exc)
    else: log.append(exc)
