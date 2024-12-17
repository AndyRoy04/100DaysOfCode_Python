
def name_format(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
name_format("andERSON", "rOY")

# leap year calculation
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
is_leap_year(2024)
