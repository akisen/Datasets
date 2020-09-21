import subprocess
import datetime
from dateutil.relativedelta import relativedelta
years = [i+2013 for i in range(7)]
months = [i+1 for i in range (12)]

for year in years:
    for month in months:
        start = datetime.datetime(year,month,1,00,00,00)
        end = start+relativedelta(months=1)
        command = 'python3 download_fits_from_JSOC_2.py "hmi.Mharp_720s" "bitmap" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        subprocess.run(command, shell=True)
        