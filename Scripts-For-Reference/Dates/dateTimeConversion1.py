from datetime import datetime

print()
#date_string = "2023-01-24T22:00:00:.000Z"

print('PoC w/ timeString:')
stackOver =    "2023-02-02T10:21:20:.000Z"
date = datetime.strptime(stackOver, '%Y-%d-%mT%H:%M:%S:.%fZ')
today = date.today()

test = date - today
print(test)


#Part 1
    #date_string1 = "2023-01-24"
    #date = datetime.strptime(date_string1, '%Y-%m-%d')

#Part 2
    #date_string1 = "2023-01-24T22:00:00"
    #date = datetime.strptime(date_string1, '%Y-%m-%dT%H:%M:%S')

#Part 3 -- stack overflow
    #stackover = "2023-02-02T10:21:20.000Z"
    #date = datetime.strptime(stackOver, '%Y-%d-%mT%H:%M:%S.%fZ')

        #Difference between dates is a colon
            # "2023-02-02T10:21:20.000Z" (stackOverFlow)
            # "2023-01-24T22:00:00:.000Z" (mine)

#PART 4 --- Final -- no doesnt work
    #stackOver = "2023-02-02T10:21:20:.000Z"
    #date = datetime.strptime(stackOver, '%Y-%d-%mT%H:%M:%S:.%fZ')

    # "2023-02-02T10:21:20:.000Z" -- (stackOverFlow)
    # "2023-01-24T22:00:00.000Z" -- (syn)
