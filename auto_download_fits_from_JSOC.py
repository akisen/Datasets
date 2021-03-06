import subprocess
import datetime
from dateutil.relativedelta import relativedelta
from retrying import retry,RetryError
from  requests.exceptions import HTTPError 
import time

years = [i+2016 for i in range(4)]
months = [i+1 for i in range (12)]
def retry_if_exception(exception):
    return isinstance(exception,HTTPError) 
@retry(retry_on_exception = retry_if_exception, wait_fixed=3600000)
def do_command(command):
     subprocess.run(command, shell=True)

for year in years:
    for month in months:
        start = datetime.datetime(year,month,1,00,00,00)
        end = start+relativedelta(months=1)
        command = 'python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "azimuth" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        do_command(command)
        time.sleep(3600)
        command = 'python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "field" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        do_command(command)
        time.sleep(3600)
        command = 'python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "inclination" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        do_command(command)
        time.sleep(3600)