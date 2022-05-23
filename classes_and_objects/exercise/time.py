class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.next_second_time = 0

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        time_in_seconds = self.time_into_seconds_conversion()
        self.next_second_time = time_in_seconds + 1
        self.conversion_seconds_into_time()
        return self.get_time()

    def time_into_seconds_conversion(self):
        seconds = 3600 * self.hours + 60 * self.minutes + self.seconds
        return seconds

    def conversion_seconds_into_time(self):
        seconds = self.next_second_time
        seconds %= 24 * 3600
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        self.hours, self.minutes, self.seconds = hour, minutes, seconds


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

time = Time(16, 35, 54)
print(time.next_second())
time = Time(1, 2, 3)
print(time.next_second())

time = Time(1, 20, 30)
print(time.get_time())


time = Time(1, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
time = Time(0, 0, 0)
print(time.next_second())