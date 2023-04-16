import time
import datetime

for i in range(3):
    time.sleep(1)
    print(f'sub1.py: {i}: {datetime.datetime.now().strftime("%H:%M:%S")}')

