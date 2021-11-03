from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import line.py

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=1)
def scheduled_job():
    execfile("line.py")
    print(datetime.datetime.today(),'This message had send')

sched.start()
