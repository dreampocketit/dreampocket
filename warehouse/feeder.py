import os, sys
sys.path.append('/root/dreampocket/dreampocket')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append('/root/dreampocket')

from warehouse.models import RawData
import csv


for row in csv.reader(open('data.csv')):
	print row	
	rawdata = RawData()
	rawdata.title = row[0]
	rawdata.context = row[1]
	rawdata.source = row[2]
	rawdata.sourcetype = row[3]
	rawdata.mainbody = row[4]
	rawdata.date = row[5]
	rawdata.author = row[6]
	rawdata.link = row[-1]
	rawdata.save()
