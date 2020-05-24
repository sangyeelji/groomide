import xml.etree.ElementTree as elemTree


singleAccountTree = elemTree.parse('00609324_2019.xml')

'''
XML TAG LIST
'''
LIST = 'list'
THIS_YEAR_VALUE = 'thstrm_amount'
ACCOUNT_NAME = 'account_nm'
FINACIAL_STATEMENTS = 'fs_div'

'''
XMK TAG TEXT FOR PARSING
자산총계  TOTAL_CAPITAL
부채총계  TOTAL_DEBT
자본총계  TOTAL_ASSETS
매출     TOTAL_SALES
영업이익  TOTAL_PROFITS
당기순이익 TOTAL_NETINCOME
'''
TOTAL_CAPITAL = '자산총계'
TOTAL_ASSETS  = '자본총계'
TOTAL_DEBT    = '부채총계'
TOTAL_SALES   = '매출액'
TOTAL_PROFITS = '영업이익'
TOTAL_NETINCOME = '당기순이익'
CONSOLIDATED_FINANCIAL_STATEMENTS = 'CFS'



root = singleAccountTree.getroot()
#print(root.tag,root.attrib)

status = root.findall('status')
#print(type(status))
#print(status[0].text)
'''
thisYearValue = root.findall(THIS_YEAR_VALUE)
for i in thisYearValue:
    print('This yesr value = ' + i)
'''
'''
def FindSepcificListFromXMLDoc(root, grandChildTagName):
    for child in root:
        for grandChild in child:
            matchList = grandChild.findall(grandChildTagName)
            print(grandChild.tag)
'''
def FindSepcificListFromXMLDoc(root, tagName):
    list = root.findall(tagName)
    return list

'''
def FindSepcificListFromXMLDocWithValueCondition(root, tagName, conditionValue):
    matchList = []
    list = root.findall(tagName)
    if(list.text == conditionValue):
        matchList.append(lis)
''' 
'''
for child in root.iter(LIST):
    for grandChild in child.iter(FINACIAL_STATEMENTS):
        if(grandChild.text == CONSOLIDATED_FINANCIAL_STATEMENTS):
            if(grandChild)
'''

basicCompanyInfo = {}
for list in root.findall(LIST):
    if(list.find(FINACIAL_STATEMENTS).text == CONSOLIDATED_FINANCIAL_STATEMENTS):
        
        if(list.find(ACCOUNT_NAME).text == TOTAL_CAPITAL):
            basicCompanyInfo[TOTAL_CAPITAL] = list.find(THIS_YEAR_VALUE).text
            
        elif(list.find(ACCOUNT_NAME).text == TOTAL_ASSETS):
            basicCompanyInfo[TOTAL_ASSETS] = list.find(THIS_YEAR_VALUE).text
            
        elif(list.find(ACCOUNT_NAME).text == TOTAL_DEBT):
            basicCompanyInfo[TOTAL_DEBT] = list.find(THIS_YEAR_VALUE).text
            
        elif(list.find(ACCOUNT_NAME).text == TOTAL_SALES):
            basicCompanyInfo[TOTAL_SALES] = list.find(THIS_YEAR_VALUE).text
            
        elif(list.find(ACCOUNT_NAME).text == TOTAL_PROFITS):
            basicCompanyInfo[TOTAL_PROFITS] = list.find(THIS_YEAR_VALUE).text
        
        elif(list.find(ACCOUNT_NAME).text == TOTAL_NETINCOME):
            basicCompanyInfo[TOTAL_NETINCOME] = list.find(THIS_YEAR_VALUE).text
            
print(basicCompanyInfo)

writeFile = open('00609324_2019.csv','w')
writeFile.write(basicCompanyInfo.keys())
