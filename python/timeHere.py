import datetime
import math

now = datetime.datetime.now().date()
startDate = datetime.datetime(2022, 2, 28).date()

daysAtKubra = abs((now - startDate).days) + 1

days = 'Day %s' % daysAtKubra
weeks = int(math.ceil(daysAtKubra / 7.0))
weeksString = 'Week %s' % weeks

print 'Time at Keap'
print weeksString
print days
