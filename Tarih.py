dayCounter = int(input('Gün sayısını giriniz='))

year = int(dayCounter/365)
month = int((dayCounter-(year*365))/30)
day = int(dayCounter-((year*365)+(month*30)))

print(f'Girdiğiniz sayı, {year} yıl {month} ay {day} güne eşittir.')