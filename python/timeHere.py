import datetime

stints = [
  {
    'stint': 1,
    'startDate': datetime.datetime(2005, 1, 27).date(),
    'endDate': datetime.datetime(2017, 9, 22).date(),
    'name': 'infusionsoft'
  },
  {
    'stint': 2,
    'startDate': datetime.datetime(2018, 1, 15).date(),
    'endDate': datetime.datetime(2019, 3, 15).date(),
    'name': 'infusionsoft/Keap'
  },
  {
    'stint': 3,
    'startDate': datetime.datetime(2022, 2, 28).date(),
    'endDate': datetime.datetime.now().date(),
    'name': 'Keap'
  }
]

current_stint_days = 0
total_days = 0

for date in stints:
    current_stint = date['stint']
    startDate = date['startDate']
    endDate = date['endDate']
    
    total_days += abs((endDate - startDate).days)
    
    if current_stint == 3:
        current_stint_days = abs((datetime.datetime.now().date() - startDate).days)
    

years, days_remainder = divmod(total_days, 365)
months, days = divmod(days_remainder, 30)

print(f'Total: {years} years, {months} months, {days} days')
    
years, days_remainder = divmod(current_stint_days, 365)
months, days = divmod(days_remainder, 30)

print(f'Current: {years} years, {months} months, {days} days')