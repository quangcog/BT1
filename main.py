import time

while True:
  current_time = time.localtime()
  formatted_time = time.strftime("%H:%M:%S", current_time)
  print(formatted_time, end="\r")
  time.sleep(1)
