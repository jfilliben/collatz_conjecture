#collatz.py

# n even: replace with n/2
# n odd:  replace with 3n+1

import random
import sys
import time

random.seed()
user_input = raw_input("Enter lower range [1]: ")
if user_input.isdigit():
    rand_min = int(user_input)
else:
    rand_min = 1
user_input = raw_input("Enter upper range [10000]: ")
if user_input.isdigit():
    rand_max = int(user_input)
else:
    rand_max = 10000
if rand_max < rand_min:
    sys.exit("Error, max cannot be less than min")
user_input = raw_input("How many repetitions? [100]: ")
if user_input.isdigit():
    num_repetitions = int(user_input)
else:
    num_repetitions = 10000
highest = (1,1,1)
print "Original_N     Max_N               Num_Steps"
for x in range(1,num_repetitions):
    original_n = random.randint(rand_min, rand_max)
    n = original_n
    max = n
    step_count = 0
    while n != 1:
        step_count += 1
        if n % 2 == 0:
            n /=  2
        else:
            n = 3 * n + 1
        if n > max:
            max = n
    if step_count > highest[2]:
        highest = (original_n, max, step_count)
    print "{0:<14} {1:<16} {2:6}".format(original_n, max, step_count)
print "Most Steps = {}".format(highest[2])
print "N = {}".format(highest[0])
print "Highest intermediate value for N = {} was {}".format(highest[0],
                                                            highest[1])

