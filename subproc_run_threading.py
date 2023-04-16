import subprocess as sb
import threading
import time
# class SbThread():
#     def __init__(self, cmd) -> None:
#         th = threading.Thread(cmd)
#         th.daemon(True)
#         th.start()

def subproc(cmd):
    return sb.run(cmd, shell=True)

th1 = threading.Thread(target=subproc, args=("python ./sub1.py",))
th1.daemon = True
th1.start()
th2 = threading.Thread(target=subproc, args=("python ./sub2.py",))
th2.daemon = True
th2.start()

# 後ろで流れているプログラム
for i in range(5):
    time.sleep(1)
    print(i)


