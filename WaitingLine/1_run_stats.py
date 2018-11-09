#!/usr/bin/python3

# ******************************************************************************
# Computing running statistics
#
# pip3 install runstats
# ******************************************************************************

from runstats import Statistics
import random

stats = Statistics()
for i in range(0, 10000):
    stats.push(random.randint(1,9))

print("count:", len(stats))
print("mean:", stats.mean())
print("stddev:", stats.stddev())
