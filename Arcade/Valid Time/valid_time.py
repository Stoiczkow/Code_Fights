def validTime(time):
    hours = range(0, 24)
    mins = range(0, 60)
    return (int(time[0:2]) in hours) and (int(time[3:]) in mins)
