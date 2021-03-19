import json

a = input()
a = json.loads(a)
res ={i['name']:[] for i in a}

def issup(cls, lst):
    for i in a:
        if cls in i['parents']:
            if i['name'] not in lst:
                lst.append(i['name'])
                issup(i['name'], lst)

for i in sorted(res):
    issup(i, res[i])
    print(f'{i} : {len(res[i])+1}')
