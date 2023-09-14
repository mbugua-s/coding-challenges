def timeConversion(s):
    time_split = s.split(":")
    seconds_am_pm = list(time_split[2])
    seconds = [seconds_am_pm[0], seconds_am_pm[1]]
    seconds = "".join(seconds)
    am_pm = [seconds_am_pm[2], seconds_am_pm[3]]
    am_pm = "".join(am_pm) # The AM or PM portion
    hours = int(time_split[0])
    
    if(hours < 12 and am_pm == 'PM'):
        hours = hours + 12
    
    elif(hours == 12 and am_pm == 'AM'):
        hours = "00"
    
    elif(hours < 10 and am_pm == 'AM'):
        hours = str(hours)
        hours = "0" + hours
    
    
    final_time = [str(hours), time_split[1], seconds]
    final_time = ":".join(final_time)
    return final_time

    """ print(hours)
    print(am_pm) """

print(timeConversion('10:40:03AM'))