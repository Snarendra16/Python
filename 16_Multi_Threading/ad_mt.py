from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers():
    for i in range(numbers):
        time.sleep(1)
        print(i)

numbers=[1,2,3,4,5,6,7,8,9,10]
if __name__=="__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        results=executor.map(print_numbers,numbers)

    for result in results:
        print(result)
