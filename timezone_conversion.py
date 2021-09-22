import pytz
from datetime import datetime

def gmt_to_asian(unix_gmt):
    asian = pytz.timezone('Asia/Kolkata')
    gmt = pytz.timezone('GMT')
    date = datetime.utcfromtimestamp(unix_gmt)
    date = gmt.localize(date)
    asian_time = date.astimezone(asian)
    return asian_time

'''
If you are unsure what string to use for 
the timezone you chose, Run this file. 
This will prints the strings for each supported timezone.
'''
if __name__ == '__main__':
    for timezone in pytz.all_timezones:
        print(timezone)
