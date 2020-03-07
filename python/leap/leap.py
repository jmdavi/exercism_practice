def leap_year(year):
    #start with general case of every four years
    if int(year) % 4 == 0:
        #check the special cases of 100 year intervals, that aren't divisible by 400
        if int(year) % 100 == 0 and int(year) % 400 != 0:
            return False
        #for non-special case of not 100 years, always True
        else: return True
    return False
