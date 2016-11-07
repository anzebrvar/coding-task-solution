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


def get_task_time(config, starting_h, starting_m):

    time_day = "today"
    time_m = starting_m
    time_h = starting_h
    minute, hour, task = config.split()
    m = minute
    h = hour

    while True:
        if minute == '*':
            m = time_m
        if hour == '*':
            h = time_h

        if int(m) == time_m and int(h) == time_h:
            solution = "%d:%02d %s - %s" % (time_h, time_m, time_day, task)
            return solution

        time_m += 1
        if time_m >= 60:
            time_h += 1
            time_m = 0
        if time_h >= 24:
            time_h = 0
            time_day = "tomorrow"


time_h, time_m = [int(x) for x in sys.argv[1].split(':')]

user_input = raw_input()
while user_input:
    print get_task_time(user_input, time_h, time_m)
    try:
        user_input = raw_input()
    except:
        user_input = None
