import time
import datetime
import random

def longstrgenerator():
    ret = ""
    for i in range(100):
        ret+=f'{random.randint(0, 1e9)}'
    return f'random message\n{ret*5}\n'

for i in range(3):
    time.sleep(1)
    print(f'sub2.py: {i}: {datetime.datetime.now().strftime("%H:%M:%S")} {longstrgenerator()}')

