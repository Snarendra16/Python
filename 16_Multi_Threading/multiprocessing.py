# Multiprocessing
# use when task is cpu bounded
# Parallel Execution i.e. using multiple cores of CPU

import Multiprocessing
# import multiprocessing.process
import time

def print_numbers():
    for i in range(4):
        time.sleep(1)
        print(i)

def print_letters():
    for i in "abcde":
        time.sleep(1.5)
        print(i)

if __name__=="__main__":

    # Creation of 2 process

    p1=multiprocessing.Process(target=print_numbers)
    p2=multiprocessing.Process(target=print_letters)
    t=time.time()

    # Starting 2 Processes

    p1.start()
    p2.start()

    # Joining main process after completion

    p1.join()
    p2.join()

finished_time=time.time()-t
print(finished_time)
