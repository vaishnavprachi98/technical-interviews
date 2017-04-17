"""
@author: David Lei
@since: 4/10/2016
@modified: 


extract the time based off the following data: Sun Dec 31 1899 06:05:00 GMT+1100 (AEDT)
need to match
- month (either Dec or Jan, can assume we don't bypass those)
- year (either 1899 or 1900, can assume we don't bypass that)
"""
import re

datetime = "Sun Dec 31 1899 06:05:00 GMT+1100 (AEDT)"

day_buffer = [0]*4
year_buffer = [0]*5

legal_month = ["Dec ", "Jan "]
legal_year = ["1899 ", "1900 "]
for i in range(5, len(datetime)):
    if datetime[i-4:i] in legal_month:
        month = datetime[i-4:i]
    elif datetime[i-5:i] in legal_year:
        year = datetime[i-5:i]
    else:
        pass
print(month)
print(len(month))
print(year)