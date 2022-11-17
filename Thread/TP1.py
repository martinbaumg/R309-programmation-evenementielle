import threading
import time
import multiprocessing


def task(i):
    print(f"Task {i} starts for {i} seconds")
    time.sleep(i)
    print(f"Task {i} ends")

T = []

for i in range(10):
    T.append(threading.Thread(target=task, args=[i]))

for i in range(len(T)):
    T[i].start()

for i in range(len(T)):
    T[i].join()


def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

if __name__ == "__main__":
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} seconds")






