import time
import random
import threading

def execute_thread(i):
    # string f time
    print("Thread {} sleeps at {}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
    
    # generate random sleep time
    rand_sleep_time = random.randint(1, 5)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
    
for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("Active Thread:", threading.activeCount())
    print("Thread Count:", threading.enumerate())