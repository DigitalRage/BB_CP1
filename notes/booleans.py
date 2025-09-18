# BB 1st Boolean Notes

import time
import datetime as date

oneslasixty = 1/60

while True:
    current_time = time.time()
    readable_time = time.ctime(current_time)
    new_current_time = date.datetime.now()
    hour = new_current_time.strftime("%H")
    # minutes = %M
    # weekday = %A, %a
    # day = %D
    # month = %B, %b
    # month num = %m
    # year = %Y, %y
    # seconds = $S
    over = True

    print(f"Current time in seconds since January 1, 1970(epoch): {current_time}")
    print(f"Current time from datetime: {new_current_time}")
    print(f"Today is: {readable_time}")
    print(f"the hour is: {hour}")

    print(f"The hour is saved as an string: {isinstance(hour, str)}")
    print(f"The hour is saved as an integer: {isinstance(hour, int)}")
    print(f"The hour is saved as an float: {isinstance(hour, float)}")
    print(hour.isalpha())


    print(f"Has a value: {bool(True)}")
    time.sleep(0.1)

    print("\033c", end="")
