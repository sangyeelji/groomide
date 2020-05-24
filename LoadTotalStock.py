import pandas
import os
import GetStockDataFromNaver

class LoadTotalStockDataCode:
	__FILE_NAME  = 'Stock_Code_From_KRX'
	__SAVEDIR    = 'StockCode'
	__CSV        = '.csv'
	
	def __init__(self):
		stockInfoList = pandas.read_html(os.path.join(LoadTotalStockDataCode.__SAVEDIR,LoadTotalStockDataCode.__FILE_NAME + LoadTotalStockDataCode.__CSV),converters={'종목코드': str})
		#pandas read_html return list of datafram even if there are only one tr/td, 
		self.stockInfoDf = stockInfoList[0]


smallInfo = LoadTotalStockDataCode()
print(smallInfo.stockInfoDf)


for i in smallInfo.stockInfoDf.index:
	stockCode = smallInfo.stockInfoDf.loc[i, '종목코드']
	stockName = smallInfo.stockInfoDf.loc[i, '회사명']
	print(stockCode)
	print(stockName)
	GetStockDataFromNaver.NaverStockData(stockCode,stockName)
	print('done')


