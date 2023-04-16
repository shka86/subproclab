import subprocess as sb
import time
import tempfile


# -----------------------------------
print("これは期待通り終わる処理。戻り値をDEVNULLで捨てているから？")
proc1 = sb.Popen('python sub2.py', shell=True, stdout=sb.DEVNULL, stderr=sb.STDOUT, encoding='utf8')
time.sleep(1)
proc2 = sb.Popen('python sub1.py', shell=True, stdout=sb.DEVNULL, stderr=sb.STDOUT, encoding='utf8')

while (proc1.poll() is None) or (proc2.poll() is None):
    time.sleep(1)
    print(f"poll: {proc1.poll()} {proc2.poll()}")
print("end")

# -----------------------------------
print("これも期待通り終わる処理。戻り値をreadlineで読んでいるから？")
proc1 = sb.Popen('python sub2.py', shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, encoding='utf8')
time.sleep(1)
proc2 = sb.Popen('python sub1.py', shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, encoding='utf8')

while (proc1.poll() is None) or (proc2.poll() is None):
    time.sleep(1)
    print(f"poll: {proc1.poll()} {proc2.poll()}")
    print(f"{proc1.stdout.readline()}")
    print(f"{proc2.stdout.readline()}")
print("end")

# -----------------------------------
print("これは期待通り終らない。stdoutが詰まっている？")
tmp1_stdout = tempfile.TemporaryFile()
tmp1_stderr = tempfile.TemporaryFile()
tmp2_stdout = tempfile.TemporaryFile()
tmp2_stderr = tempfile.TemporaryFile()

proc1 = sb.Popen('python sub2.py', shell=True, stdout=tmp1_stdout, stderr=tmp1_stderr, encoding='utf8')
time.sleep(1)
proc2 = sb.Popen('python sub1.py', shell=True, stdout=tmp2_stdout, stderr=tmp2_stderr, encoding='utf8')

while (proc1.poll() is None) or (proc2.poll() is None):
    time.sleep(1)
    print(f"poll: {proc1.poll()} {proc2.poll()}")
print("end")

# -----------------------------------
print("これは期待通り終らない。stdoutが詰まっている？")
proc1 = sb.Popen('python sub2.py', shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, encoding='utf8')
time.sleep(1)
proc2 = sb.Popen('python sub1.py', shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, encoding='utf8')

while (proc1.poll() is None) or (proc2.poll() is None):
    time.sleep(1)
    print(f"poll: {proc1.poll()} {proc2.poll()}")
print("end")