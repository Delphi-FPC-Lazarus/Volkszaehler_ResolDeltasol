#!/bin/sh

# Vorbereiten
cd /home/pi
#rm measurements.xml
#rm measurements.sql
rm resol.json
rm resol.sql

# Stecagrid
#wget http://192.168.1.251/measurements.xml
#python ./measurements.python > measurements.sql
#mysql --user=root --password=raspberry --database=volkszaehler < measurements.sql

# Resol
cd resol
python resol.py > ../resol.json
cd ..
python ./resoljsontosql.py > resol.sql
mysql --user=root --password=raspberry --database=volkszaehler < resol.sql

