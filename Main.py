import os
import json
import glob

ile = 0

def countPerPerson(data, path):
    totalNum = 0
    parcipants = []
    result = glob.glob(path+data+'/*.json')
    for j in result:
        with open(j, 'r') as f:
            data = json.load(f)
            for l in data['messages']:
                totalNum += 1
            for k in data['participants']:
                if k['name'] not in parcipants and k['name'] != 'Kuba Przybysz':
                    parcipants.append(k['name'].encode('iso-8859-1').decode('utf-8'))
    return parcipants, totalNum


for i in os.listdir('data/messages/inbox/'):
    print(countPerPerson(i, 'data/messages/inbox/'))
    ile += 1
print(ile)
