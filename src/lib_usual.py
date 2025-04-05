import os
import sys
import math
import cmath
import ctypes
import time
import random
import dill
import threading
import numpy
import customtkinter                as ctk
from   ctypes                       import Union
from   queue                        import Queue
from   src.HighPrecisionType        import (
                                            HighPrecisionFloat as HPF, 
                                            HighPrecisionInt   as HPI, 
                                            )
from   src.high_precision_operation import (
                                            HighPrecisionOperation   as HPO,
                                            HighPrecisionOperationEX as HPO_EX
                                            )


def read_settings(file_path):
    settings = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        list_settings = file.readlines()
        for i in list_settings:
            if i[0] == '#':
                continue
            else:
                settings[i.split('=')[0]] = i.split('=')[1].strip()
    return settings

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()