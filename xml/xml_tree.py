import xml.etree.ElementTree as ET

rgb = {'red': 0, 'green': 0, 'blue':0}
root = ET.fromstring(input())

def search(root, n=1):
    for i in root:
        rgb[i.attrib['color']] += n
        search(i, n+1)
        
search(root)
for i in sorted(rgb):
    print(rgb[i], end = ' ')
