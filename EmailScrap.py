import re
import json
from collections import Counter
file = open('websiteData.txt', 'r', encoding='utf-8')
f = file.read()
h = re.findall('[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*', f)
count = Counter(h)
emails = {}
for i in h:
    emails[i] = {}
    emails[email]['Occurance'] = h.count(i)
    a = i.split('@')
    if (len(a[0]) <= 8):
        emails[i]['EmailType'] = 'Non-human'
    else:
        emails[i]['EmailType'] = 'Human'
print(emails)
# to_json=open('result.json','w')
# to_json=json.dump(emails,to_json)
