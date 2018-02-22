import sys
import subprocess


proc = subprocess.Popen(['ssh localhost'], shell=True)
proc.communicate()

print ('Run another gdb process. This proves that we can just re-use sys.stdin.')

proc = subprocess.Popen(['ssh localhost'], shell=True)
proc.communicate()
