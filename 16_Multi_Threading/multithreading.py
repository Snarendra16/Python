import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in "abcde":
        time.sleep(1)
        print(letter)

t1=threading.Thread(target=print_letters)
t2=threading.Thread(target=print_numbers)

t=time.time()
t1.start()
t2.start()

t1.join()
t2.join()
Finished_time=time.time()-t
print(Finished_time)