import sys

from datetime import datetime
import time

from data_generate import getdata
import median

def reloaddata():
	if len(sys.argv) > 1:
		if sys.argv[1] == '-r':
			return True
	return False

arr = getdata( reloaddata() )

start_time = datetime.now()

median.nlogn_median(arr)

#median.quickselect_median(arr)

print(datetime.now() - start_time)