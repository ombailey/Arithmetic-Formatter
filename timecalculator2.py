def add_time (starttime, duration, sday = 'none'.title()):
    s_time = []
    d_time = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    minute = 60
    hours = 60
    day = 24
    daysplit = 12
    morning = 'AM'
    night = 'PM'
    n = 0

#Creating a List of the different characters in start time and duration time.
    for digit in starttime:
        s_time = starttime.split(':')

    for digit in duration:
        d_time = duration.split(':')

# Getting the hour and minutes value of starttime provided.
    starthour = int(s_time[0])
    s_minutes = s_time[1].split()
    startminutes = int(s_minutes[0])

#Getting the hour and minutes value of duration provided.
    dur_hours = int(d_time[0])
    dur_minutes = int(d_time[1])

#Adding Together the Minutes and Hours
    finalminutes = int(startminutes) + int(dur_minutes)
    finalhour = starthour + dur_hours

    if finalminutes >= minute:
        add_hour = finalminutes // hours 
        finalhour = finalhour + add_hour
        finalminutes = finalminutes - minute

    if len(str(finalminutes)) < 2:
        finalminutes = str(finalminutes).zfill(2)

#Determining Time of Day
    stimeofday= s_minutes[1]
    stimeisam = (stimeofday == morning)
    stimeispm = (stimeofday == night)
    timeofday = s_minutes[1]
    finaltimeofday = ""
    fhours = finalhour

    for round in range(finalhour // daysplit):
        timeisam = (timeofday == morning)
        timeispm = (timeofday == night)

        if timeisam == True and fhours >= daysplit:
            timeofday = night
        elif timeisam == True and fhours <= daysplit:
            timeofday = morning
        elif timeispm == True and fhours >= daysplit:
            timeofday = morning
        elif timeispm == True and fhours <= daysplit:
            timeofday = night
        fhours = fhours - daysplit

    finaltimeofday = timeofday
    timeisam = (timeofday == morning)
    timeispm = (timeofday == night)

#Showing double zeros for time
    if finalminutes == 0:
        finalminutes = '00'

#Adding up days later and Outputting result
    if finalhour >= daysplit and stimeispm is True:
        n += (finalhour // day) + 1

    if finalhour >= day and stimeisam is True:
        n += (finalhour // day) + 1

    if (finalhour//day) == 1 and stimeisam is True:
        n = 1

    if (finalhour//day) == 1 and timeispm is True:
        n = 1

    if finalhour <  day and stimeisam is True:
        n = 0

    if n == 1:
        dayslater = 'next day'
    
    else:
        dayslater = f'{n} days later'

#Restarting Time when its passed 24 hours. 
    finalhour = finalhour - (day * (finalhour // day))  

#Restarting Time at 0 when its passed 12 hours.
    if finalhour > daysplit and (timeispm == True or timeisam == True):
        finalhour = finalhour - daysplit

    if finalhour == 0:
        finalhour = 12

#Determining Day of the Week
    if sday != 'None':
        daynum = days.index(str(sday).title())
        for num in range(n):
            daynum += 1
        if daynum >= 6:
            daynum = 0
        finalday = days[daynum]
    if sday == 'None':
        if n == 0:
            print (f'{finalhour}:{finalminutes} {finaltimeofday}')
        else:
            print (f'{finalhour}:{finalminutes} {finaltimeofday} ({dayslater})')

#Print Final day of the week when day is specified
    if sday != 'None':
        if n == 0:
            print (f'{finalhour}:{finalminutes} {finaltimeofday}, {finalday}')
        else:
            print (f'{finalhour}:{finalminutes} {finaltimeofday}, {finalday} ({dayslater})')
