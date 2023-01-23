from datetime import datetime

print()
#POC to find greatest / least date out of list
print('Find greatest date / least date: ')
dates = ['2023-01-24T22:00:00.000Z',
 '2023-03-29T22:00:00.000Z', 
 '2023-02-10T22:00:00.000Z',
 '2012-01-20T22:08:00.000Z',
 '2023-01-19T22:00:00.000Z',
 '2025-01-19T22:00:00.000Z']

print(min(dates))
print(max(dates))


#POC w/ common date type
print()
print('Poc w/ common date type: ')
timestamps = ['2011-06-2', 
'2020-08-05', 
'2019-02-04', 
'2029-1-14', 
'2014-12-13'] 
dates = [datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
dates.sort()
sorteddates = [datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
print(sorteddates)

####
print()
print('Poc w/ UN-common date type: ')
timestamps = ['2015-01-24T22:00:00.000Z',
 '2012-03-29T22:00:00.000Z', 
 '2023-02-10T22:00:00.000Z',
 '2029-01-20T22:08:00.000Z',
 '2011-01-19T22:00:00.000Z',
 '2025-01-19T22:00:00.000Z'] 
dates = [datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ") for ts in timestamps]
dates.sort()
sorteddates = [datetime.strftime(ts, "%Y-%m-%dT%H:%M:%S.%fZ") for ts in dates]
print(sorteddates)


