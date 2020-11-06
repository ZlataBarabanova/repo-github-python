import sys
hour, rate_one_hour, premium = map(float, sys.argv[1:])
print('wage - {}'.format(hour * rate_one_hour + premium))