import time
import os
import urllib2
from random import randint
import sys 

def check():
    url = "https://raw.githubusercontent.com/sushilshinde/config/master/fl.txt?r=" + str(randint(1,10000))
    for line in urllib2.urlopen(url):
        print(line)
        if(len(line) > 1):
            os.system("git pull && cp empthy_fl.txt fl.txt && git add . && git commit -m 'Resetting' && git push")
            os.system("killall -9 'Google Chrome'")
            os.system("pmset sleepnow")
while True:
    time.sleep(10)
    check()