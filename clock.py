from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import os
os.system("line.py")

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=1)
def scheduled_job():
    print(datetime.datetime.today(),'This message had send')
    execfile("line.py")


sched.start()
