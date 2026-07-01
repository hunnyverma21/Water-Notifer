import time
from plyer import notification

def water_reminder():
 while True:
        notification.notify(
            title="Water Reminder For Hunny",
            message="Time to drink water and stay hydrated.",
            timeout=10
        )
        time.sleep(3600)

water_reminder()