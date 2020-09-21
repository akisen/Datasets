from sunpy.net import jsoc
from sunpy.net import attrs as a
from datetime import datetime as dt
import datetime 
import astropy.units as u
import os
import glob
import calendar
client = jsoc.JSOCClient()
years = [i+2013 for i in range(7)]
months = [i+2 for i in range(11)]
def remove_glob(pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(p):
            os.remove(p)
for year in years:
    for month in months:
        days = [day+1 for day in range(calendar.monthrange(year, month)[1])]
        for day in days:
            start = datetime.datetime(year,month,day,00,00,00)
            end =start+datetime.timedelta(days=1)
            print(start,end)
            response = client.search(a.Time(start,end),a.jsoc.Series('hmi.Mharp_720s'),a.Sample(1*u.hour) ,a.jsoc.Notify("f20c012d@mail.cc.niigata-u.ac.jp")) #開始時間のところに等号を入れられなかったので調整 
            path = "/media/akito/Data/Mharp/bitmap/"+str(year)+"/"+str(year)+str(month).zfill(2)
            res = response.client.fetch(response,path=path)
            rm_path1= path+"/"+"*.magnetogram.fits"
            rm_path2 = path+"/"+"*.mask.fits"
            remove_glob(rm_path1)
            remove_glob(rm_path2)
