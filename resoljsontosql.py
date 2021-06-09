import json
import re

with open("resol.json") as json_format_file: 
  resoljson = json.load(json_format_file)
  
resoljsonroot = resoljson["DeltaSol BS 2009"]

# Kollektortemperatur (entities 16 2ed03d20-c950-11eb-a986-fd2195d4a96e)
value = resoljsonroot["Temperatur Sensor 1"]
value = re.sub('[^0-9.]', '', value)
value = value.replace('nan', '0')
sql1 = 'insert into data (channel_id, timestamp, value) values (16, unix_timestamp()*1000,%s);' % (value)

# Fuehler unten (entities 13 1c26b290-97c9-11ea-9c01-11ed7286b899)
value = resoljsonroot["Temperatur Sensor 2"]
value = re.sub('[^0-9.]', '', value)
value = value.replace('nan', '0')
sql2 = 'insert into data (channel_id, timestamp, value) values (13, unix_timestamp()*1000,%s);' % (value)

# Fuehler oben (entities 14 0d1da960-a014-11ea-985e-e9d8eac2fe2e)
value = resoljsonroot["Temperatur Sensor 3"]
value = re.sub('[^0-9.]', '', value)
value = value.replace('nan', '0')
sql3 = 'insert into data (channel_id, timestamp, value) values (14, unix_timestamp()*1000,%s);' % (value)

# Kesseltemperatur (entities 15 74e335c0-c94e-11eb-a752-512e21a0807b)
value = resoljsonroot["Temperatur Sensor 4"]
value = re.sub('[^0-9.]', '', value)
value = value.replace('nan', '0')
sql4 = 'insert into data (channel_id, timestamp, value) values (15, unix_timestamp()*1000,%s);' % (value)

# Abschluss
sqlq = 'quit';

print(sql1)
print(sql2)
print(sql3)
print(sql4)
print(sqlq)

