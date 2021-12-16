#Program to find loss and profit percentage
#Profit percentage = (Profit /Cost Price) × 100
#Loss percentage = (Loss / Cost price) × 100

CostPrice = float(input('Enter the Cost Price :'))
SellingPrice = float(input("Enter the selling Price :"))

if SellingPrice > CostPrice:
 profit = SellingPrice - CostPrice
 profitPercent = round(((profit/CostPrice)*100),4) 
 print(f'Profit Percentage : {profitPercent}%') 

else:
 loss = CostPrice - SellingPrice 
 lossPercent = round(((loss/CostPrice)*100),4)

 print(f'Loss Percentage : {lossPercent}% ')