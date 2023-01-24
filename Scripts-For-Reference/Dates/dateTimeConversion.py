from datetime import datetime, date
print()

#Take list of strings and subtract current date
dates = ['19 March, 2023', '19 April, 2023', '22 April, 2023']
today = date.today()
daysList = []


#Step 1 - convert dates from string into object (date_object)
#Step 2 - find difference in days (days_difference)
#Step 3 - append info from (days_difference) into (daysList)
#Step 4 - print daysList
for date in dates:
    date_object = datetime.strptime(date, '%d %B, %Y').date()
    days_difference = (date_object - today).days
    daysList.append(days_difference)

print('Poc w/ list:')
print(daysList)



#####
#Singular date PoC:
print()
print('PoC w/ 1 date:')
date_string = "19 March, 2023"
date = datetime.strptime(date_string, '%d %B, %Y')
today = date.today()

test = date - today
print(test)


#####
print()
#date_string = "2023-01-24T22:00:00:.000Z"

print('PoC w/ timeString:')
date_string1 = "2023-01-24T22:00:00:.000Z"
date = datetime.strptime(date_string1, '%Y-%d-%mT%H:%M:%S.%fZ')
today = date.today()

test = date - today
print(test)


#Part 1
    #date_string1 = "2023-01-24"
    #date = datetime.strptime(date_string1, '%Y-%m-%d')


#Part 2
    #date_string1 = "2023-01-24T22:00:00"
    #date = datetime.strptime(date_string1, '%Y-%m-%dT%H:%M:%S')

#Part 3
    #continued


#datetime.datetime.fromisoformat('2019-01-04T16:41:24+02:00')
#date = datetime.strptime(date_string1, '%Y-%m-%dT%H:%M:%S')


#%Y-%m-%dT%H:%M:%S:.%Z
#%Y-%d-%mT%H:%M:%S.%fZ




