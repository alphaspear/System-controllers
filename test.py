import schedule
import time
import subprocess
def send_wol():
    mac_address = "3C:7C:3F:81:C0:B8"
    subprocess.call(["wakeonlan",mac_address])

print("started")
while(1):
    print("going sleep for 5")
    time.sleep(5)
    send_wol()
    print("exec done")
