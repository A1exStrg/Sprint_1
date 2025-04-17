time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
new_time = time_str.split(',')
minute_all = 0

for value in new_time:
    parts_of_time = value.split()
    for part in parts_of_time:
        if 'h' in part:
            hour = int(part.replace('h', ''))
            minute_all += hour * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            minute_all += minutes
        elif 's' in part:
            second = int(part.replace('s', ''))
            minute_all += second // 60
print(minute_all)

