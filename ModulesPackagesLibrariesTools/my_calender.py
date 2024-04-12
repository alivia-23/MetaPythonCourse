import sys
import calendar
locations = sys.path
for i in locations:
    print(i)

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)