import requests
import re

URL1 = input()
URL2 = input()

def res(url1, url2):
    response = requests.get(url1)
    pat = r'<a href="(.+)">'
    if response.ok:
        for link in re.findall(pat, response.text):
            resp = requests.get(link)
            if resp.ok:
                for link2 in re.findall(pat, resp.text):
                    if link2 == url2:
                        return 'Yes'
        return 'No'            
    else:
        return 'No'
    
print(res(URL1, URL2))
