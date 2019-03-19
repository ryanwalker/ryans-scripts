import datetime

now = datetime.datetime.now().date()
startDate = datetime.datetime(2019, 3, 18).date()

daysAtKubra = abs((now - startDate).days)

val = 'Days at Kubra: %s' % daysAtKubra
print val
