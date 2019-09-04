import os
from google.cloud import datastore
import json

#for exporting query result as json on local using legacy sql, --n stands for limit,'[]' used becoz of legacy sql
os.system("bq --format=prettyjson query --n=100 'SELECT * FROM [solid-future-247118:my_dataset.new_table]' > fordatastore_table.json")

#loading the json file, it is a list containing dictionaries
data=json.loads(open('fordatastore_table.json').read())

#google api datastore

client = datastore.Client()
x=1
length = len(data)

#for going in each dictionaries of list
for i in range(length):
    
   
    key = client.key('bigquerytest', x)
    entity = datastore.Entity(key=key)
    entity.update(
        data[i]
        
    )
    client.put(entity)
# Then get by key for this entity
    result = client.get(key)
    print(result)
    x=x+1






