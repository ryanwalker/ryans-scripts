import datetime
import math

now = datetime.datetime.now().date()
startDate = datetime.datetime(2019, 3, 18).date()

daysAtKubra = abs((now - startDate).days) + 1

days = 'Day %s' % daysAtKubra
weeks = int(math.ceil(daysAtKubra / 7.0))
weeksString = 'Week %s' % weeks

print 'Time at KUBRA'
print weeksString
print days
