import time
import winsound
from plyer import notification


def reminder():
    winsound.Beep(1000, 500)
    notification_title = "Hydration Reminder"
    notification_message = "Its Time To Drink Some Water"
    notification.timeout = 10
    notification.notify(title=notification_title, message=notification_message)


def main():
    interval_hours = 1
    while True:
        wait_time = interval_hours * 60 * 60
        time.sleep(wait_time)
        reminder()


if __name__ == "__main__":
    main()
