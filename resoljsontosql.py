import json
import re

with open("resol.json") as json_format_file: 
  resoljson = json.load(json_format_file)
  
resoljsonroot = resoljson["DeltaSol BS 2009"]

value = resoljsonroot["Temperatur Sensor 2"]
value = re.sub('[^0-9.]', '', value)
value = value.replace('nan', '0')
sql1 = 'insert into data (channel_id, timestamp, value) values (13, unix_timestamp()*1000,%s);' % (value)
sql2 = 'quit';

print(sql1)
print(sql2)
