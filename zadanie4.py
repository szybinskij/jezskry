import time

from random import randint
r=1000000
long_list = [randint(0, 3000) for element in range(r)]

start_time = time.perf_counter()
for x in range(r):
    if long_list==(-1):
        print('mamy cieu')

stop_time = time.perf_counter()
elapsed_time = stop_time - start_time
print('Start 1', start_time)
print('Stop 1', stop_time)
print('Pomiar 1', elapsed_time)

start_time = time.perf_counter()
if -1 not in long_list:
    pass
else:
    print('mamy cieu')
stop_time = time.perf_counter()
print('Start 2', start_time)
print('Stop 2', stop_time)
print('Pomiar 2', elapsed_time)