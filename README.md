
# Coding task solution

The solution is written in Python2, so you can run it with

    python check_scheduled_time.py 16:10

Configuration is written in a separate file (in this case 
hardcoded to `scheduler.conf`).

This solution is using one while loop to iterate over minutes
from the time passed as a parameter until all the solutions are
found and then printed in the same order as passed in scheduler
configuration (ordering assumed from example output).

Possible extensions/improvements:
 - error handling (invalid scheduler config)
 - hour parameter validation
