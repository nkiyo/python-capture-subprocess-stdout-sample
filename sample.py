import sys
import subprocess

print('>> start parent process')

# TODO pythonの子プロセスを起動する

# C++の子プロセスを起動する
cmd = "./cpp-subprocess"
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("waiting...")
stdout_str, stderr_str = proc.communicate()
print(f"stdout:{stdout_str} stderr:{stderr_str}")
print('<< end parent process')

# TODO

