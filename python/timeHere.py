from datetime import datetime, timedelta

stints = [
  {
    'stint': 1,
    'startDate': datetime(2005, 1, 27).date(),
    'endDate': datetime(2017, 9, 22).date(),
    'name': 'infusionsoft'
  },
  {
    'stint': 2,
    'startDate': datetime(2018, 1, 15).date(),
    'endDate': datetime(2019, 3, 15).date(),
    'name': 'infusionsoft/Keap'
  },
  {
    'stint': 3,
    'startDate': datetime(2022, 2, 28).date(),
    'endDate': datetime.now().date(),
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
        current_stint_days = abs((datetime.now().date() - startDate).days)
    

years, days_remainder = divmod(total_days, 365)
months, days = divmod(days_remainder, 30)

print(f'\n\tTotal: {years} years, {months} months, {days} days')
    
years, days_remainder = divmod(current_stint_days, 365)
months, days = divmod(days_remainder, 30)

print(f'\tCurrent: {years} years, {months} months, {days} days\n')




current_date = datetime.now().date()

delta = timedelta(days=total_days)

# Subtract the timedelta from the current date to get the desired date
desired_date = current_date - delta

# print("\t(Effective Date", total_days, "days ago:", desired_date, ")")
