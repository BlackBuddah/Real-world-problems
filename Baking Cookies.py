##'''
##Author:Adesina Osibodu
##Date:08-30-2023
##Purpose:Week Two Exercise
##'''
##
###Declaring Variables
##Salesproj=0.0
##profit=0.0
##
##
###Data types: Integers,Floats, and String
##salesproj=float(input('Enter projected sales'))
##
###Calculation for Profit
##profit=salesproj*0.23
##
##print('This is my profit',profit)
##

Flour = 2.75
Sugar = 1.5
Butter = 1.0

Cookies = 48

CookiesNeeded = int(input('Enter number of cookies to be made: '))

CalculateFlour = Flour * (CookiesNeeded / Cookies)
CalculateSugar = Sugar * (CookiesNeeded / Cookies)
CalculateButter = Butter * (CookiesNeeded / Cookies)

print('Number of Flour: ' + str(CalculateFlour))
print('Number of Butter: ' + str(CalculateButter))
print('Number of Sugar: ' + str(CalculateSugar))
