import shutil
import os
import glob
years = [2010+i for i in range(9)]
months = [i+1 for i in range (12)]

for year in years:
    paths = set(glob.glob("/media/akito/Data/HMI_REGION/%s/*.fits" % (year)))
    for month in months:
        if (year==2010 and month<6):
            continue
        os.makedirs("/media/akito/Data/HMI_REGION/%s/%s%s" % (year,year, str(month).zfill(2)),exist_ok=True)
        for path in paths:
            if (int(path.split(".")[2][0:4])==year) and int(path.split(".")[2][4:6])==month:
                print(path)
                shutil.move(path,"/media/akito/Data/HMI_REGION/{0}/{0}{1}/{2}".format(year,str(month).zfill(2),path.split("/")[-1]))