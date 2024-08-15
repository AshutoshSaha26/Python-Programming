class Time:
    def __init__(self, hour, min, sec):
        self.__hour = hour
        self.__min = min
        self.__sec = sec
    def __add_time(self, hour, min, sec):
        total_seconds = (self.__hour * 3600 + self.__min * 60 + self.__sec) + (hour * 3600 + min * 60 + sec)
        hour = total_seconds // 3600
        min = (total_seconds % 3600) // 60
        sec = total_seconds % 60
        return hour, min, sec
    def add(self, other_time):
        hour, min, sec = self.__add_time(other_time.__hour, other_time.__min, other_time.__sec)
        print(f"Added Time: {hour} hours, {min} minutes, {sec} seconds")
if __name__ == "__main__":
    time1 = Time(1, 45, 30)  
    time2 = Time(2, 30, 45)  
    time1.add(time2)
