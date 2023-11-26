# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

#Counting the number of days in the specific year and month indicated as input
def countdays(year, month, day):
    count = 0
    weeks = calendar.monthcalendar(year, month)
    for i in weeks:
        if i[day] != 0:
            count += 1
    return count

run = True
while(run):
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or 'exit' to quit")

        day = input("Which day do you want to count")
        if day == "exit":
            run = False
            break
        newday = int(day)

        year = input("Choose the year:")
        newyear = int(year)

        month = input("Choose the month:")
        newmonth = int(month)

        result = countdays(newyear , newmonth, newday)
        print(str(result))

    except Exception as e:
        print("Sorry ", e, " was not a valid input")
