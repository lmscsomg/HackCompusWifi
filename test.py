__author__ = 'lms'
import multiprocessing

password = 0
def f (start, end, target, fin):
    for i in range(start, end+10):
        password = i
        if fin.is_set():
            print 'Other process found target, exit'
            return
        if i == target:
            print 'Target: ' + str(password) + ' Found'
            fin.set()
            return


if __name__ == "__main__":
    fin = multiprocessing.Event()
    size = 240
    target = 890
    for start in (1, 259, 510, 760):
        multiprocessing.Process(target = f, args = (start, start+size, target, fin)).start()