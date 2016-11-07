"""

sample input

30 1 /bin/run_me_daily
45 * /bin/run_me_hourly
* * /bin/run_me_every_minute
* 19 /bin/run_me_sixty_times


sample output for 16:10

1:30 tomorrow - /bin/run_me_daily
16:45 today - /bin/run_me_hourly
16:10 today - /bin/run_me_every_minute
19:00 today - /bin/run_me_sixty_times

"""

import sys

if len(sys.argv) <= 1:
    print "Please specify the current time in HH:MM format."

time_h, time_m = [int(x) for x in sys.argv[1].split(':')]
time_day = "today"
config = []

for line in open('scheduler.conf'):
    config.append(line.split())

solutions = [None]*len(config)


while None in solutions:

    for i in range(len(config)):
        minute, hour, task = config[i]

        if minute == '*':
            minute = time_m
        if hour == '*':
            hour = time_h

        if int(minute) == time_m and int(hour) == time_h and solutions[i] is None:
            solutions[i] = "%d:%02d %s - %s" % (time_h, time_m, time_day, task)

    time_m += 1
    if time_m >= 60:
        time_h += 1
        time_m = 0
    if time_h >= 24:
        time_h = 0
        time_day = "tomorrow"


for s in solutions:
    print s
