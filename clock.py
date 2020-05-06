import sys
import time


class clock:

    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        # self.dates = 1

    def settime(self,seconds = 0,minutes = 0,hours = 0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    def begins(self):
        try:
            while True:
                self.seconds += 1
                if self.seconds >= 60:
                    self.minutes += 1
                    self.seconds = 0
                if self.minutes >= 60:
                    self.hours += 1
                    self.minutes = 0
                if self.hours >= 24:
                    self.hours = 0
                time.sleep(1)
                print(f"{self.hours}:{self.minutes}:{self.seconds}" ,end ='\r',flush =True)
                # sys.stdout.flush()
        except KeyboardInterrupt:
            print("Your Clock Stopped")
start = clock()
hrs = int(input("hrs: "))
mins = int(input("minutes: "))
sec = int(input("Seconds: "))
start.settime(sec,mins,hrs)
start.begins()
