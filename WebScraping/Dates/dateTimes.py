import datetime


#print any date
print()
d = datetime.date(2023, 4, 3)
print('Any date: '  + str(d))

print()
today = datetime.date.today()
print('Today: ' + str(today)) 
print('Todays Year: ' + str(today.year)) 
print('Todays Month: ' + str(today.month)) 
print('Todays Day: ' + str(today.day)) 


#timeDeltas - difference between 2 times
print()
print('Deltas: ')
print('Todays date: ' + str(today))
today = datetime.date.today()
oneWeek = datetime.timedelta(days=7)
newDate = today + oneWeek
print('One week from todays date: ' + str(newDate))

print()
#days till bday
print('Subtracting dates: ')
bday = datetime.date(2023, 4, 3)
till_bday = bday - today
print('Days till bday: ' + str(till_bday))
print('Days till bday: ' + str(till_bday.days))
print('Seconds till bday: ' + str(till_bday.total_seconds()))
#print('Seconds till bday: ' + str(till_bday.


print()









