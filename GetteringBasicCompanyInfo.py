import requests
import os
import xml.etree.ElementTree as ET
#https://opendart.fss.or.kr/api/fnlttSinglAcnt.xml?crtfc_key=xxxxxxxxxxxxxxxxxx&corp_code=00126380&bsns_year=2018&reprt_code=11011
#https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=9cb99dacf06918fac2a4d6c8c886b01498c57d4b
class GetBasicCompanyInfoFromOpenDart:
    __URL     = 'https://opendart.fss.or.kr/api/fnlttSinglAcnt.xml?crtfc_key=9cb99dacf06918fac2a4d6c8c886b01498c57d4b'
    __SAVEDIR = 'CompanyFinancialReport'
    __CSV     = '.csv'
    __URL_YEAR = '&bsns_year='
    __URL_REPORT_CODE = '&reprt_code='
    __URL_COMP_CODE = '&corp_code='
    
    TOTAL_CAPITAL = '자산총계'
    TOTAL_ASSETS  = '자본총계'
    TOTAL_DEBT    = '부채총계'
    TOTAL_SALES   = '매출액'
    TOTAL_PROFITS = '영업이익'
    TOTAL_NETINCOME = '당기순이익'
    CONSOLIDATED_FINANCIAL_STATEMENTS = 'CFS'
    
    LIST = 'list'
    THIS_YEAR_VALUE = 'thstrm_amount'
    ACCOUNT_NAME = 'account_nm'
    FINACIAL_STATEMENTS = 'fs_div'
    #URL = dartOpenApiUrl + singleMainAccount + authKey + compcode + year + reprt_code
    
    def __init__(self, companyCode, year, reportCode):
        self.companyCode = companyCode
        self.year = year
        self.reportCode = reportCode
        
        if not(os.path.isdir(GetBasicCompanyInfoFromOpenDart.__SAVEDIR)):
            os.makedirs(GetBasicCompanyInfoFromOpenDart.__SAVEDIR)
    
    def GetDataFromOpenDart(self):
        url = GetBasicCompanyInfoFromOpenDart.__URL + GetBasicCompanyInfoFromOpenDart.__URL_COMP_CODE + self.companyCode + GetBasicCompanyInfoFromOpenDart.__URL_YEAR + self.year + GetBasicCompanyInfoFromOpenDart.__URL_REPORT_CODE + self.reportCode
        res = requests.get(url)
        
        print(url)
        
        return res.text
    
    def ChangeFromTextToXML(self):
        rawXMLText = self.GetDataFromOpenDart()
        corpXmlTree = ET.ElementTree(ET.fromstring(rawXMLText))
        root = corpXmlTree.getroot()
        status = root.findall('status')
        if( status[0].text == '000'):
            return root
        else:
            raise Exception('No Data')
    
    def GetBasicInfoFromXMLRoot(self):
        try:
            root = self.ChangeFromTextToXML()
        except :
            print('NO DATA ERR FROM OPEN DART')
            return 0
        basicCompanyInfo = {}
        for list in root.findall(GetBasicCompanyInfoFromOpenDart.LIST):
            if(list.find(GetBasicCompanyInfoFromOpenDart.FINACIAL_STATEMENTS).text == GetBasicCompanyInfoFromOpenDart.CONSOLIDATED_FINANCIAL_STATEMENTS):
                if(list.find(GetBasicCompanyInfoFromOpenDart.ACCOUNT_NAME).text == GetBasicCompanyInfoFromOpenDart.TOTAL_CAPITAL):
                    basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_CAPITAL] = list.find(GetBasicCompanyInfoFromOpenDart.THIS_YEAR_VALUE).text.replace(',', '')
                elif(list.find(GetBasicCompanyInfoFromOpenDart.ACCOUNT_NAME).text == GetBasicCompanyInfoFromOpenDart.TOTAL_ASSETS):
                    basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_ASSETS] = list.find(GetBasicCompanyInfoFromOpenDart.THIS_YEAR_VALUE).text.replace(',', '')
                elif(list.find(GetBasicCompanyInfoFromOpenDart.ACCOUNT_NAME).text == GetBasicCompanyInfoFromOpenDart.TOTAL_DEBT):
                    basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_DEBT] = list.find(GetBasicCompanyInfoFromOpenDart.THIS_YEAR_VALUE).text.replace(',', '')
                elif(list.find(GetBasicCompanyInfoFromOpenDart.ACCOUNT_NAME).text == GetBasicCompanyInfoFromOpenDart.TOTAL_SALES):
                    basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_SALES] = list.find(GetBasicCompanyInfoFromOpenDart.THIS_YEAR_VALUE).text.replace(',', '')
                elif(list.find(GetBasicCompanyInfoFromOpenDart.ACCOUNT_NAME).text == GetBasicCompanyInfoFromOpenDart.TOTAL_PROFITS):
                    basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_PROFITS] = list.find(GetBasicCompanyInfoFromOpenDart.THIS_YEAR_VALUE).text.replace(',', '')
                elif(list.find(GetBasicCompanyInfoFromOpenDart.ACCOUNT_NAME).text == GetBasicCompanyInfoFromOpenDart.TOTAL_NETINCOME):
                    basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_NETINCOME] = list.find(GetBasicCompanyInfoFromOpenDart.THIS_YEAR_VALUE).text.replace(',', '')
        self.basicCompanyInfo = basicCompanyInfo
        
    def WriteCurrentData(self):
        targetFileName = os.path.join(GetBasicCompanyInfoFromOpenDart.__SAVEDIR, self.companyCode + GetBasicCompanyInfoFromOpenDart.__CSV)
        if not (os.path.exists(targetFileName)):
            with open(targetFileName, 'w') as f:
                f.write(GetBasicCompanyInfoFromOpenDart.TOTAL_CAPITAL)
                f.write(',')
                f.write(GetBasicCompanyInfoFromOpenDart.TOTAL_ASSETS)
                f.write(',')
                f.write(GetBasicCompanyInfoFromOpenDart.TOTAL_DEBT)
                f.write(',')
                f.write(GetBasicCompanyInfoFromOpenDart.TOTAL_SALES)
                f.write(',')
                f.write(GetBasicCompanyInfoFromOpenDart.TOTAL_PROFITS)
                f.write(',')
                f.write(GetBasicCompanyInfoFromOpenDart.TOTAL_NETINCOME)
                f.write('\n')
        
        with open(targetFileName, 'a') as f:
            f.write(self.year)
            f.write(',')
            f.write(self.basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_CAPITAL])
            f.write(',')
            f.write(self.basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_ASSETS])
            f.write(',')
            f.write(self.basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_DEBT])
            f.write(',')
            f.write(self.basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_SALES])
            f.write(',')
            f.write(self.basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_PROFITS])
            f.write(',')
            f.write(self.basicCompanyInfo[GetBasicCompanyInfoFromOpenDart.TOTAL_NETINCOME])
            f.write('\n')
        
if __name__ == "__main__":
    year = 2019
    while year>0:
        BasicInfo = GetBasicCompanyInfoFromOpenDart('00126380',str(year),'11011') #00126380 삼성전자 사업보고서
        status = BasicInfo.GetBasicInfoFromXMLRoot()
        if status != 0:
            BasicInfo.WriteCurrentData()
            year = year - 1
        else:
            break


        
        
    
	