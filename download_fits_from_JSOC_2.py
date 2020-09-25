"""
download_fits_from_JSOC.py
自動でFitsファイルをJSOCサーバからダウンロードしてくるスクリプト
コマンドライン引数でダウンロードしてくるデータの種類と期間を指定する
実行例:python3 download_fits_from_JSOC.py "HMI.ME_720s_fd10" "azimuth" "2011-04-01" "2011-05-01"
参考:https://docs.sunpy.org/en/0.7/generated/api/sunpy.net.jsoc.JSOCClient.html
"""
import astropy.units as u
from sunpy.net import jsoc
from sunpy.net import attrs as a
from datetime import datetime as dt
import datetime 
import sys
import urllib.request
client = jsoc.JSOCClient()

args = sys.argv
start = args[3]
end = args[4]
response = client.search(a.Time(start,end),a.jsoc.Series(args[1]),a.Sample(1*u.hour),a.jsoc.Notify("akitrb001@gmail.com"),jsoc.Segment(args[2])) 
path = "/media/akito/Data21"+"/"+str(args[1])+"/"+str(start[:4])+"/"+str(start[:4])+str(start[5:7])
res = response.client.fetch(response,path=path)
print(response)