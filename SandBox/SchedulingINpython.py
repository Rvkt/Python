import time
import schedule


def get_time() -> str:

    return time.strftime("%X (%d/%m/%y)")


def task():
    print('Doing task ......', get_time())


# schedule.every(5).seconds.do(task)
# schedule.every(5).minutes.do(task)
# schedule.every(5).hours.do(task)
# schedule.every(5).days.do(task)
# schedule.every(5).weeks.do(task)

schedule.every().minutes.at(':10').do(task)

# schedule.every().day.at('09:49').do(task)


while True:
    schedule.run_pending()
    time.sleep(1)
