import re
import json
file = open('websiteData.txt', 'r', encoding='utf-8')
f = file.read()
h = re.findall('[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*', f)
emails = {}
for i in h:
    emails[i] = {}
    emails[i]['Occurance'] = h.count(i)
    a = i.split('@')
    if re.findall('\S+\.\S+@\S+', i) or (len(a[0]) >= 8):
        emails[i]['EmailType'] = 'Human'
    else:
        emails[i]['EmailType'] = 'Non-Human'
print(emails)
to_json = open('result.json', 'w')
to_json = json.dump(emails, to_json)
