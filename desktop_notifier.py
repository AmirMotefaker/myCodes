# Code by AmirMotefaker

# Desktop Notifier

# Solution 1 - basic
# import time
# from plyer import notification
# # plyer: Platform-independent wrapper for platform-dependent APIs

# if __name__ == "__main__":
#     while True:
#         notification.notify(
#             title = "ALERT!!!",
#             message = "Rest! Now is the time to walk!",
#             timeout = 10
#         )
#         time.sleep(15)
    

# Solution 2 - advanced

import time
from win10toast import ToastNotifier
# win10toast: An easy-to-use Python library for displaying Windows 10 Toast Notifications

reminder_Time = input("Input Time in 24hr format(HH:MM:SS) to set reminder-> ")
rem_message = input("Enter your message:> ")

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == reminder_Time:
        print(current_time)
        break;
notify = ToastNotifier()
notify.show_toast("Notification",rem_message)
