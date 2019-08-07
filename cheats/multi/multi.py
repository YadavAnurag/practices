import threading
import time

x = 0

def increment():
    global x 
    x += 1


def threadTask(lock):
    global x 
    lock.acquire()
    while x<10000000:
        increment()
    lock.release()

def mainTask():
    global x 
    x = 0
    lock = threading.Lock()

    allThreads = set()
    for _ in range(10):
        threadObject = threading.Thread(target=threadTask, args=(lock,))
        allThreads.add(threadObject)
    
    for singleThread in allThreads:
        singleThread.start()

    for singleThread in allThreads:
        singleThread.join()



if __name__ == '__main__':
    startTime = time.time()
    mainTask()
    endTime = time.time()
    print('totalTime {} x = {}'.format(startTime-endTime, x))
