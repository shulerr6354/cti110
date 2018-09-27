#Sales Prediction
#9/27/18
#CTI-110 P2T1 - Sales Prediction
#Ronald Shuler
#


#Get the projected total sales
total_sales = float(input('Enter the projected sales: $'))

#Calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

#Display
print('The total profit is $', format(profit, ',.2f'))
