import os
import re
import operator
import pprint

counter_fail = {}
counter_error = {}
pattern_fail = re.compile(r'^FAIL:\s(\w*\s\([\w.]*\))')
pattern_error = re.compile(r'^ERROR:\s(\w*\s\([\w.]*\))')
for fn in os.listdir('.'):
    if os.path.isfile(fn):
        f = open(fn)
        lines = f.readlines()
        f.close()
        fails = []
        print(len(lines))
        for line in lines:
            t = pattern_fail.findall(line)
            if len(t) > 0:
                counter_fail[t[0]] = counter_fail.get(t[0], 0) + 1
            u = pattern_error.findall(line)
            if len(t) > 0:
                counter_error[t[0]] = counter_fail.get(t[0], 0) + 1

sorted_fails = sorted(counter_fail.items(), key=operator.itemgetter(1), reverse=True)
sorted_errors = sorted(counter_fail.items(), key=operator.itemgetter(1), reverse=True)
for key in sorted_fails:
    print()
pp=pprint.PrettyPrinter(width=150)
print('FAILS')
pp.pprint(sorted_fails)
print('ERRORS')
pp.pprint(sorted_errors)
