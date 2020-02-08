import datetime


def week_get(d):
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    print('---'.join([str(date_from), str(date_to)]))


week_get(datetime.datetime.now())

date_list = []
for i in range(0, 7):
    date_list.append(((datetime.datetime.now() - datetime.timedelta(days=i)).month,
                      (datetime.datetime.now() - datetime.timedelta(days=i)).day))
print(date_list)