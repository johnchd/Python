from datetime import datetime

###Strptime python is used to convert string to datetime object.
#Strftime converts date object to a string date.


print()
#date_string = "2023-01-24T22:00:00:.000Z"

print('PoC w/ timeString:')
final =          "2023-01-24T22:00:00.000Z"
date = datetime.strptime(final, "%Y-%m-%dT%H:%M:%S.%fZ")
today = date.today()

test = date - today
print(test)



#PART 4 --- Final
    #final =          "2023-01-24T22:00:00.000Z"
    #date = datetime.strptime(final, "%Y-%m-%dT%H:%M:%S.%fZ")


###############
###############
###############
###############

print()
#Take list of strings and subtract current date
dates = ['2023-01-24T22:00:00.000Z', '2023-03-29T22:00:00.000Z', '2023-02-10T22:00:00.000Z', '2023-01-20T22:08:00.000Z', '2023-01-19T22:00:00.000Z']
today = date.today()
daysList = []


#Step 1 - convert dates from string into object (date_object)
#Step 2 - find difference in days (days_difference)
#Step 3 - append info from (days_difference) into (daysList)
#Step 4 - print daysList
for date in dates:
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    days_difference = (date_object - today).days
    daysList.append(days_difference)

print('Poc w/ list:')
print(daysList)


































