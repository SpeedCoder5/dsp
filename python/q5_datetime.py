# Hint:  use Google to find python function
from datetime import datetime, timedelta

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
_ds = datetime.strptime(date_start, '%m-%d-%Y')
_de = datetime.strptime(date_stop, '%m-%d-%Y')
_td = _de - _ds # create a datetime.timedelta
print _td.days, "days"

####b)
date_start = '12312013'  
date_stop = '05282015'
_ds = datetime.strptime(date_start, '%m%d%Y')
_de = datetime.strptime(date_stop, '%m%d%Y')
_td = _de - _ds # create a datetime.timedelta
print _td.days, "days"

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'
_ds = datetime.strptime(date_start, '%d-%b-%Y')
_de = datetime.strptime(date_stop, '%d-%b-%Y')
_td = _de - _ds # create a datetime.timedelta
print _td.days, "days"

