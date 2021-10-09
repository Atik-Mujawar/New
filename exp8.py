# import  _thread 
# import time

# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       #print "%s: %s" % ( threadName, time.ctime(time.time()) )
#       print (threadName,time.ctime(time.time()))

# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print("Error: unable to start thread")

# while 1:
#    pass

print("---------------------------------------------------------------------------------------")

import threading
import time
e = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)
# def print_time(threadName, counter, delay):
#     while counter:
#         if e:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time()))
#         counter-=1

# Create new threads
t1=threading.myThread(1, "Thread-1", 1)
t2=threading.myThread(2, "Thread-2", 2)
# Start new Threads
t1.start()
t2.start()
print("Exiting Main Thread")