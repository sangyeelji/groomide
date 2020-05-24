siginifcantShareHoldertotalAsset = 919200000000
ROEList = [3.81,15.41,20.16]
avgROE = 15
requiredEarningRate = 7.9
totalNumStock = 37865000

totalValueOfComp = siginifcantShareHoldertotalAsset + ((siginifcantShareHoldertotalAsset*(avgROE-requiredEarningRate))/requiredEarningRate)

print(totalValueOfComp)
print(totalValueOfComp/totalNumStock)

excessIncome = siginifcantShareHoldertotalAsset + (siginifcantShareHoldertotalAsset*(avgROE-requiredEarningRate))



inexpensive = siginifcantShareHoldertotalAsset + excessIncome*(0.7/(1+requiredEarningRate-0.7))
print(inexpensive)
print(inexpensive/totalNumStock)

soso = siginifcantShareHoldertotalAsset + excessIncome*(0.9/(1+requiredEarningRate-0.9))
print(soso)
print(soso/totalNumStock)
