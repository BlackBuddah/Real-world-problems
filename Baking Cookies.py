

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
