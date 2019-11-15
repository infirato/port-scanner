import socket
import subprocess
from datetime import datetime
import sys
import time
if len(sys.argv) != 2:
    time.sleep(1)
    sys.exit("\33[91mUsage: scan-port.py 192.168.1.1\33[0m")
subprocess.call("clear",shell=True)
RemoteIp = socket.gethostbyname(sys.argv[1])
print("+="*30)
print("\33[33mScanning Host:\33[0m",RemoteIp)
print("+="*30)
t1 = datetime.now()
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((RemoteIp,port))
        if result == 0:
            print("Port{}: Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("Exiting")
    time.sleep(1)
    sys.exit()
except socket.gaierror:
    print("Hostname Doesnt Exist. exiting....")
    time.sleep(1)
    sys.exit()
except socket.error:
    print("Could Not connect to the host. exiting....")
    time.sleep(1)
    sys.exit()
t2 = datetime.now()
total = t1 = t2
print("Scanning Completed in:",total)
sys.exit()
