import datetime
import time

class Pomodoro(object):

    def __init__(self, timer_length=25):
        self.timer_length = datetime.timedelta(minutes=timer_length)

    def format_time(self, seconds):
        return ("{0:.0f}:{1:02d}".format(seconds//60, int(seconds%60)))

    def print_time(self, seconds):
        print(self.format_time(seconds))

    def get_seconds_left(self):
        delta = datetime.datetime.now() - self.start_time
        return (self.timer_length-delta).total_seconds()
        
    def print_seconds_left(self):
        self.print_time(self.get_seconds_left())

    def start_timer(self):
        self.start_time = datetime.datetime.now()
        self.print_seconds_left()
        while True:
            time.sleep(1)
            seconds_left = self.get_seconds_left()
            if seconds_left < 0:
                break
            self.print_time(seconds_left)
        
def main():
    pomo = Pomodoro(1)
    pomo.start_timer()

if __name__ == '__main__':
    main()
