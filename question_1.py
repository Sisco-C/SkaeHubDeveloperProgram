def leapyear_checker(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
 
year = 2100
if(leapyear_checker(year)):
    print(bool())
else:
    print(bool())