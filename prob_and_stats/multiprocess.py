import multiprocessing
import time
def worker(k):
    print(f"starting process {i}")
    time.sleep(10)
    print('done waiting')
    return

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()