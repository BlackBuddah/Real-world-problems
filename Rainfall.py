

#Declaring Variables
Years = 0
Month = 0
Average = 0
Rainfall = 0.0

#Ask user for the number of years

years=int(input('Enter number of years:'))

#Initial variable

TotalInchesofRainfall=0
TotalMonths=years * 12
Averagerainfallpermonth=TotalInchesofRainfall/TotalMonths


#Outerloop

for year in range(1,years+1):
    
#Innerloop
    
    for month in range(1,13):
        print('year',year,'month',month )
        Rainfall=float(input('Total inches for month:'))

       
        TotalInchesofRainfall += Rainfall
         

#Average
        
Average=TotalInchesofRainfall/TotalMonths

#output

print(f'Number of Months: {TotalMonths}')
print(f'Total inches of Rainfall: {TotalInchesofRainfall}')
print(f'Average rainfall per month: {Average:.2f} inches') 
