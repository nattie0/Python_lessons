import requests, sys

for i in sys.stdin:
    resp = requests.get(f'http://numbersapi.com/{i}/math?json=true')
    r = resp.json()
    if r['found']:
        print('Interesting')
    else: print('Boring')
