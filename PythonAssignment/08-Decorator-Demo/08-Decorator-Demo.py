from asyncio import sleep
import time

def time_this(function):
    def inner(*args, **kwargs):
        begin = time.time()
        print("Running " + function.__name__)         
        function(*args, **kwargs)
        end = time.time()
        duration = str(end - begin)
        print(function.__name__ + " ran in " + duration + " seconds")
    return inner

@time_this
def sleeper_func(sleeptime):
	print(f'sleeping for {sleeptime}')
	sleep(sleeptime)
	return 'Woke up!'

sleeper_func(2)