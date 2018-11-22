import datetime

for year in range(1006, 1996): # year must start with 1 and end with 6
    if year % 4 == 0 and str(year)[3] == '6': # checking if year is a leap year and if it ends in a 6
        date = datetime.date(year, 1, 26)
        if date.weekday() == 0: # checking if date is a monday
            print(date) 
            
            # clue1: "he ain't the youngest, he is the second" ---> 1/26/1756
            # clue2: "buy flowers for tomorrow" ---> 1/27/1756
            # Mozart's birthday