import os
import re
import sys
import time
from dateutil import rrule
import datetime
from collections import defaultdict


records = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    records = f.read().splitlines()
    records.sort()

# Test Data
# records = ['[1518-11-01 00:00] Guard #10 begins shift',
#            '[1518-11-01 00:05] falls asleep',
#            '[1518-11-01 00:25] wakes up',
#            '[1518-11-01 00:30] falls asleep',
#            '[1518-11-01 00:55] wakes up',
#            '[1518-11-01 23:58] Guard #99 begins shift',
#            '[1518-11-02 00:40] falls asleep',
#            '[1518-11-02 00:50] wakes up',
#            '[1518-11-03 00:05] Guard #10 begins shift',
#            '[1518-11-03 00:24] falls asleep',
#            '[1518-11-03 00:29] wakes up',
#            '[1518-11-04 00:02] Guard #99 begins shift',
#            '[1518-11-04 00:36] falls asleep',
#            '[1518-11-04 00:46] wakes up',
#            '[1518-11-05 00:03] Guard #99 begins shift',
#            '[1518-11-05 00:45] falls asleep',
#            '[1518-11-05 00:55] wakes up']

record_pattern = re.compile(r'\[(.*)\]\s(\w+)(?:\s#(\d+))?')
guard_times = defaultdict(lambda: {'total_sleep': 0,
                                   'minutes_asleep': defaultdict(lambda: 0)})
for record in records:
    m = record_pattern.search(record)
    date, action, guard_id = m.groups()
    # Convert to datetime so we can do maths with it
    date  = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')

    if action == 'Guard':
        current_guard = guard_id
    elif action == 'falls':
        start_time = date
    elif action == 'wakes':
        for dt in rrule.rrule(rrule.MINUTELY, dtstart=start_time, until=date + datetime.timedelta(minutes=-1)):
            guard_times[current_guard]['minutes_asleep'][dt.minute] += 1
        # Get total time asleep in that session
        start_ts = time.mktime(start_time.timetuple())
        stop_ts = time.mktime(date.timetuple())
        guard_times[current_guard]['total_sleep'] += int(stop_ts-start_ts) / 60
        start_time = None


guard = max(guard_times, key=lambda key: guard_times[key]['total_sleep'])
minute = max(guard_times[guard]['minutes_asleep'], key=guard_times[guard]['minutes_asleep'].get)

print(f"Part 1: {int(guard) * minute}")
