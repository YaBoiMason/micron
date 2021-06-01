import datetime
import sys
import time
import math
import random
import re

class LibraryFunctions():
    def lib_print(args):
        for i in args:
            print(i)

    def lib_concat(args):
        buf = ""
        for i in args:
            buf += i
        return buf

    def lib_input(args):
        return input(args[0])

    def lib_split(args):
        return args[0].split(args[1])

    def lib_format(args):
        toFmt = args.pop(0)
        return toFmt.format(*args)

    def lib_day(args):
        return datetime.datetime.today().day

    def lib_month(args):
        return datetime.datetime.today().month

    def lib_year(args):
        return datetime.datetime.today().year

    def lib_hour(args):
        return datetime.date.today().hour

    def lib_minute(args):
        return datetime.date.today().min

    def lib_second(args):
        return datetime.date.today().second

    def lib_ms_unix(args):
        return time.time_ns() 

    def lib_sleep(args):
        time.sleep(args[0])

    def lib_timefmt(args):
        return datetime.date.today().strftime(args[0])

    def lib_pi(args):
        return math.pi

    def lib_e(args):
        return math.e

    def lib_ceil(args):
        return math.ceil(args[0])

    def lib_floor(args):
        return math.floor(args[0])

    def lib_log(args):
        return math.log(args[0], args[1])

    def lib_sqrt(args):
        return math.sqrt(args[0])

    def lib_sin(args):
        return math.sin(args[0])

    def lib_cos(args):
        return math.cos(args[0])

    def lib_radtodeg(args):
        return math.degrees(args[0])

    def lib_degtorad(args):
        return math.radians(args[0])

    def lib_randomint(args):
        return random.randint(args[0], args[1])

    def lib_randomfloat(args):
        return random.uniform(args[0], args[1])

    def lib_randomseed(args):
        random.seed(args[0])

    def lib_regex(args):
        return re.match(args[0], args[1])

    def lib_open(args):
        file = open(args[0])
        data = file.read()
        file.close()
        return data

    def lib_write(args):
        file = open(args[0], "w")
        file.write(args[1])
        file.close()

    def lib_exit(args):
        sys.exit(args[0])