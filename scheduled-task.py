import schedule
import time
import os
def send_wol():
    mac_address = "3C:7C:3F:81:C0:B8"
    command = "wakeonlan "+ mac_address
    os.system(command)

schedule.every().day.at("04:53").do(send_wol)

while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for a second between checks

