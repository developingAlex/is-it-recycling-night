# script to tell me if its recycling bin collection day with with a normal 
# english sentence answer to the question: "when is recycling pickup?":
# "Today"
# "Not Today"   (if today is a normal garbage day)
# "Tomorrow"
# "Not Tomorrow"   (if tomorrow is a normal garbage day)
# "This coming collection day"
# "Not this coming collection day"

import datetime

known_recycling_day = "2018-04-10"

# converts a string of format yyyy-mm-dd into a datetime date object
def string_to_date(date_str):
  return datetime.date.today() # placeholder, tbc

# takes two dates and returns a boolean indicating whether the number of days 
# difference between the two dates is a multiple of 14
def fortnight_falls(date1, date2):
  return False #placeholder, tbc

# same as fortnight falls but will return true if the day difference between
#  the two dates is a mutliple of 7 instead of 14
def weekly_falls(date1, date2):
  return False #placeholder, tbc

def tomorrow():
  return datetime.date.today() + datetime.timedelta(1)

today = datetime.date.today()

if fortnight_falls(known_recycling_day, today):
  # then today is a recycling day
  pass
elif fortnight_falls(known_recycling_day, tomorrow()):
  # then tomorrow is a recycling day
  pass
elif weekly_falls(known_recycling_day, today):
  # then today is not recycling day
  pass
elif weekly_falls(known_recycling_day, tomorrow()):
  # then tomorrow is not recycling day
  pass
else:
  # tbc, "This coming collection day" or "Not this coming collection day" 
  pass
