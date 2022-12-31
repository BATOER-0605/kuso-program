import schedule
import time
import subprocess

def doit():
    print('Working.../')
    time.sleep(60)

    #do jobs
    subprocess.run('./launch.sh')
    print('\nDone\n')

schedule.every().day.at('23:59').do(doit)

while True:
  schedule.run_pending()
  time.sleep(10)