# script to tell me if its recycling bin collection day with with a normal 
# english sentence answer to the question: "when is recycling pickup?":
# "Today"
# "Not Today"   (if today is a normal garbage day)
# "Tomorrow"
# "Not Tomorrow"   (if tomorrow is a normal garbage day)
# "This coming collection day"
# "Not this coming collection day"

import datetime


last_known_recycling_day = datetime.date(2018,4,10)

# takes two dates and returns a boolean indicating whether the number of days 
# difference between the two dates is a multiple of 14
def fortnight_falls(date1, date2):
  difference = date1 - date2
  return (difference.days % 14 == 0)

# same as fortnight falls but will return true if the day difference between
#  the two dates is a mutliple of 7 instead of 14
def weekly_falls(date1, date2):
  difference = date1 - date2
  return (difference.days % 7 == 0)

def tomorrow():
  return datetime.date.today() + datetime.timedelta(1)

def when_is_recycling_pickup():
  today = datetime.date.today()

  if fortnight_falls(last_known_recycling_day, today):
    # then today is a recycling day
    return "Today"
  elif fortnight_falls(last_known_recycling_day, tomorrow()):
    # then tomorrow is a recycling day
    return "Tomorrow"
  elif weekly_falls(last_known_recycling_day, today):
    # then today is not recycling day
    return "Not today"
  elif weekly_falls(last_known_recycling_day, tomorrow()):
    # then tomorrow is not recycling day
    return "Not tomorrow"
  else:
    # if difference days % 14 > 7 it implies that we are now approaching another
    # recycling day, therefore the answer should be "this coming..."
    # if however the difference days % 14 < 7 then it should imply that we have
    # recently had a collection and therefore it won't be this coming ("Not this 
    # coming...")
    if (last_known_recycling_day - today).days % 14 > 7:
      return "This coming collection day"
    else:
      return "Not this coming collection day"
  
print("When is the next recycling day you ask?")
print(when_is_recycling_pickup())