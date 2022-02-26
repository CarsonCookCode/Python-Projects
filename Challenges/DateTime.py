import datetime
import pytz

tzLondon = pytz.timezone('Europe/London')
tzPortland = 'PST8PDT'
tzNYC = 'America/New_York'
def isOpen():
    print("get")

print(datetime.datetime.now(tzLondon))
print(datetime.datetime.now(tzPortland))
print(datetime.datetime.now(tzNYC))
