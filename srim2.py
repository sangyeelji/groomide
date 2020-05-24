import requests
import lxml
import xml.etree.ElementTree as ET
import os

dartOpenApiUrl = 'https://opendart.fss.or.kr/'
AllfinancialUrl = 'api/fnlttSinglAcntAll.xml'
singleMainAccount = '/api/fnlttSinglAcnt.xml'
authKey = '?crtfc_key=9cb99dacf06918fac2a4d6c8c886b01498c57d4b'
compcode = '&corp_code=00609324'
year = '&bsns_year=2019'
reprt_code = '&reprt_code=11011'
fs_div = '&fs_div=OFS'

URL = dartOpenApiUrl + financialUrl + authKey + compcode + year + reprt_code + fs_div
URL = dartOpenApiUrl + singleMainAccount + authKey + compcode + year + reprt_code


res = requests.get(URL)
#print(URL)
fullDocFile = open("00609324_2019.xml",mode='w')
fullDocFile.write(res.text)
fullDocFile.close()

