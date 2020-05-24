import requests
import sys
import zipfile
import os
import xml.etree.ElementTree as ET

dartOpenApiUrl = 'https://opendart.fss.or.kr/'
financialUrl = 'api/fnlttSinglAcnt.xml'
authKey = '?crtfc_key=9cb99dacf06918fac2a4d6c8c886b01498c57d4b'
compcode = '&corp_code=005930'
year = '&bsns_year=2018'
reprt_code = '&reprt_code=11011'
fs_div = '&fs_div=OFS'
getCoprCode = 'https://opendart.fss.or.kr/api/corpCode.xml'

finalURL = dartOpenApiUrl + financialUrl + authKey + compcode + year + reprt_code + fs_div
#print(dartOpenApiUrl + financialUrl + authKey + compcode + year + reprt_code + fs_div)
#print('	https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json?crtfc_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&corp_code=00356370&bsns_year=2018&reprt_code=11011&fs_div=OFS')

#print(getCoprCode + authKey)
#뷰웍스 00609324
res = requests.get(getCoprCode + authKey)

corpCodeFile = open('corpCodeFile.zip', mode = 'wb')
corpCodeFile.write(res.content)

#corpXmlData = open('corpCodeFile/CORPCODE.xml', mode = 'rt')
corpXmlTree = ET.parse('corpCodeFile/CORPCODE.xml')
root = corpXmlTree.getroot()

print(root.tag)
print(root.attrib)
count = 0
for child in root:
	for item in child:
		print(item.tag)
		print(item.text)
	
	count = count + 1
	
print(count)





















