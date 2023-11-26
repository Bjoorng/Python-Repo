#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now()
    
    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("current year: %y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("current year: %Y"))
    print(now.strftime("%a, %d %B, %y")) #Upper case letters mean the full name of the corresponding value while lower case letters correspond to the abbreviated version

    #### Time Formatting ####
    print(now.strftime("Locale Date and Time: %c"))
    print(now.strftime("Locale Date: %x"))
    print(now.strftime("Locale Time: %X"))
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print (now.strftime("Current time: %H:%M:%S")) # 24-Hour:Minute:Second:AM
    print (now.strftime("12-hour time: %I:%M %p")) # 12-Hour:Minute

if __name__ == "__main__":
    main()
