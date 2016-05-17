from time import gmtime, strftime
import time
import os
import sys

if len(sys.argv)==1:
	T = gmtime()
else:
	date = sys.argv[1]
	T = time.strptime(date,"%d%b%Y")

contd='''\\newentry{{ {month} {day}, {year} }}'''

Year  = int(strftime("%Y",T))
Month = int(strftime("%m",T))
Day   = int(strftime("%d",T))
Week  = int(strftime("%W",T))
date_string = strftime("%Y%b%d",T)

hash_code = "{year:03X}{week:02X}{month:01X}{day:02X}".format(
	year  = (2**12)-Year,
	month = (2**8 )-Month,
	day   = (2**8 )-Day,
	week  = (2**8 )-Week,
)


filename = "Entries/{}-{}.tex".format(hash_code,date_string)
if os.path.isfile(filename):
	print "Log {} Exists".format(filename)
else:
	with open(filename,"w") as f:
		f.write(contd.format(
			month = strftime("%b",T),
			day   = Day,
			year  = Year,
		))
	print("Created File {}".format(filename))
