# Code by amotef@gmail.com

# Desktop Notifier

# Solution 1 - basic
import time
from plyer import notification
# plyer: Platform-independent wrapper for platform-dependent APIs

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Rest! Now is the time to walk!",
            timeout = 10
        )
        time.sleep(15)
    
