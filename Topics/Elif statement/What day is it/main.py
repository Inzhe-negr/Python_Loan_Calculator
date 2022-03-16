hour = 10
shift = int(input())
zone_hour = hour + shift
if zone_hour < 0:
    print("Monday")
elif zone_hour >= 24:
    print("Wednesday")
else:
    print("Tuesday")
