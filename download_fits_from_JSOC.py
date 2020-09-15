from sunpy.net import jsoc
from sunpy.net import attrs as a
from datetime import datetime as dt
import datetime 
client = jsoc.JSOCClient()

with open ("kesson.txt","r") as f: 
    data = f.read()
    data = data.split("\n")
    data = [dt.strptime(time,'%Y-%m-%d　 %H:%M:%S') for time in data]
# start = data[0]-datetime.timedelta(seconds=1)
# end = data[0]+datetime.timedelta(seconds=44)
start = datetime.datetime(2010,5,1,00,00,00)
end = datetime.datetime(2010,5,1,1,00,00)
print(start,end)
response = client.search(a.Time(start,end),a.jsoc.Series('hmi.m_45s'), a.jsoc.Notify("f20c012d@mail.cc.niigata-u.ac.jp")) 
res = response.client.fetch(response,path="/media/akito/Data/HMI_REGION/Missing_data")
print(response)