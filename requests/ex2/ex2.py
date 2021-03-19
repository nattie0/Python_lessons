import re, requests
URL = input()
res = set()
for i in re.findall(r'''<a.*href=['"](?:.*?://)?([\w.-]+?)[/:'"]''', requests.get(URL).text):
    if i[0] != '.':
        res.add(i)
res = list(res)
res.sort()
print(*res, sep='\n')
