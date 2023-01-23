from datetime import datetime, timedelta, date


print()
dueDate = '2023-03-19 18:36:55.523839'
print('Due date:      ' + dueDate)

currentDate = datetime.now()
print("Current date:  " + str(currentDate))
#print(datetime.now() + timedelta(days=5, hours=-5))


#works but not really useful
print()
new = currentDate - timedelta()
print('Current date (minus) 5 days: ' + str(new))

print()
currentDate = datetime.now()



dueDate = '2023-03-19 18:36:55.523839'
currentDate = datetime.now()

####
YearDateTime = currentDate.strftime("%Y/%m/%d")
print('YearDateTime: ', YearDateTime)

#newDueDate = dueDate.strftime("%Y/%m/%d")
#print('newDueDate: ', newDueDate)











