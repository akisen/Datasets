import subprocess
import datetime
from dateutil.relativedelta import relativedelta
from retrying import retry
years = [i+2013 for i in range(7)]
months = [i+1 for i in range (12)]

def retry_if_exception(exception):
    return isinstance(exception,Exception) 
@retry(retry_on_exception = retry_if_exception, wait_fixed=3600000)
def do_command(command):
     subprocess.run(command, shell=True)

for year in years:
    for month in months:
        start = datetime.datetime(year,month,1,00,00,00)
        end = start+relativedelta(months=1)
        command = 'python3 download_fits_from_JSOC_2.py "hmi.Mharp_720s" "bitmap" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        do_command(command)