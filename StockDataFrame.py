import pandas
import numpy
import os

class LoadStockData:
	__SAVEDIR = 'SavedStock'
	__CSV     = '.csv'
	__RECALED = '_recaled'
	
	def __init__(self,stockCode):
		self.stockCode = stockCode
		
	def read_csv_recaled_data(self):
		dataFrame = pandas.read_csv(os.path.join(LoadStockData.__SAVEDIR, self.stockCode + LoadStockData.__RECALED + LoadStockData.__CSV),sep=',')
		return dataFrame
	
	def read_csv_data(self):
		dataFrame = pandas.read_csv(os.path.join(LoadStockData.__SAVEDIR, self.stockCode + LoadStockData.__CSV),sep=',')
		return dataFrame
	
	
	
  
samsung = LoadStockData('005930')
hynix = LoadStockData('000660')
samsungStockDataFrame = samsung.read_csv_recaled_data()
hynixStockDataFrame = hynix.read_csv_data()


sEndPrice = pandas.concat([samsungStockDataFrame['date'],samsungStockDataFrame['end_price']],axis = 1)
hEndPrice = pandas.concat([hynixStockDataFrame['date'],hynixStockDataFrame['end_price']],axis = 1)
cbEf = pandas.concat([sEndPrice,hEndPrice],axis = 1)
print(cbEf)
cbEf = cbEf.fillna(0)
print(cbEf)
cbEf = cbEf.loc[::-1]
print(cbEf)
cbEf.to_csv(os.path.join('SavedStock','new' + '.csv'),mode='a', header=False, index=False)

#print(cbEf.corr())


