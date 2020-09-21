import subprocess
import datetime
from dateutil.relativedelta import relativedelta
years = [i+2011 for i in range(9)]
months = [i+1 for i in range (12)]

for year in years:
    for month in months:
        start = datetime.datetime(year,month,1,00,00,00)
        end = start+relativedelta(months=1)
        command = 'python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "azimuth" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        subprocess.run(command, shell=True)
        command = 'python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "field" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        subprocess.run(command, shell=True)
        command = 'python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "inclination" '+str(start.year)+'-'+str(start.month).zfill(2)+'-01 "'+str(end.year)+'-'+str(end.month).zfill(2)+'-01"'
        print(command)
        subprocess.run(command, shell=True)