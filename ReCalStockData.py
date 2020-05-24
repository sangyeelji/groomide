import pandas
import os
import datetime

#Re-calculate for stock splite
class ReCalStockData:
	__SAVEDIR = 'SavedStock'
	__CSV     = '.csv'
	__RECALED = '_recaled'
	
	def __init__(self,stockCode,recalStartDate,rate):
		self.stockCode = stockCode
		self.recalStartData = datetime.datetime.strptime(recalStartDate,"%Y.%m.%d").date()
		self.rate = rate
		
		targetFileName = os.path.join(ReCalStockData.__SAVEDIR,self.stockCode + ReCalStockData.__CSV)
		dataFrame = pandas.read_csv(os.path.join(ReCalStockData.__SAVEDIR,self.stockCode + ReCalStockData.__CSV),sep=',')
		self.dataFrame = dataFrame
	
	def reCalAndSave(self):
		for i in self.dataFrame.index:
			val = self.dataFrame.loc[i, 'date']
			val = datetime.datetime.strptime(val,"%Y.%m.%d").date()
			if val <= self.recalStartData:
				self.dataFrame.loc[i, 'start_price'] = self.dataFrame.loc[i, 'start_price']/self.rate
				self.dataFrame.loc[i, 'end_price'] = self.dataFrame.loc[i, 'end_price']/self.rate
				self.dataFrame.loc[i, 'high'] = self.dataFrame.loc[i, 'high']/self.rate
				self.dataFrame.loc[i, 'low'] = self.dataFrame.loc[i, 'low']/self.rate
				self.dataFrame.loc[i, 'price_change'] = self.dataFrame.loc[i, 'price_change']/self.rate
				
		stockFile = open(os.path.join(ReCalStockData.__SAVEDIR,self.stockCode + ReCalStockData.__RECALED + ReCalStockData.__CSV), mode='wt', encoding='utf-8')
		stockFile.write('date,end_price,price_change,start_price,high,low,quantity')
		stockFile.close()
		self.dataFrame.to_csv(os.path.join(ReCalStockData.__SAVEDIR,self.stockCode + ReCalStockData.__RECALED + ReCalStockData.__CSV),mode='a', header=False, index=False)
				
test = ReCalStockData('005930','2018.05.03',50)
test.reCalAndSave()

        