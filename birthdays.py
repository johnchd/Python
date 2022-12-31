#!/usr/bin/env python3

birthdays = {'john': 'april 3rd', 'steven': 'feb 2nd'}


while True:
    print('Enter a name to see their birthday: (or enter nothing to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + "'s birthday is "  + birthdays[name])
        
    else:
        print('I do not have the birthday of ' + name)
        print('What is there birthday?')
        noBirthday = input()
        birthdays[name] = noBirthday
        print('Info has been updated.')
    
