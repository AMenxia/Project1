#!/usr/bin/env python3
import shutil
import psutil
def check_disk_usage():
    du= shutil.disk_usage("/")
    free = du.free/du.total*100
    print( ("{}% of disk space is free").format(free))

def check_cpu_usage():
    print( str(psutil.cpu_percent(2)) + "% of CPU is being used")
    if psutil.cpu_percent(2)<70:
        print ("CPU is healthy")
    else:
        print("He's struggling Jim X0")

check_disk_usage()
check_cpu_usage()