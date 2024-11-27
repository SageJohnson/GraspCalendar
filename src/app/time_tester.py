import datetime

class DatetimeSimulator:
    def __init__(self, year, month, day, hour, minute, second):
        self.user_datetime = datetime.datetime(year, month, day, hour, minute, second)
        print("created " + str(self.user_datetime))

    def add_time(self, hours):
        new_datetime = self.user_datetime + datetime.timedelta(hours=hours)
        return new_datetime

    def subtract_time(self, hours):
        new_datetime = self.user_datetime - datetime.timedelta(hours=hours)
        return new_datetime

    def get_current_datetime(self):
        return datetime.datetime.now()
    
    def get_simulated_datetime(self):
        return datetime.datetime.now()
    
    def to_string(self):
        return self.user_datetime.timetz().strftime("%D    %H:%M")