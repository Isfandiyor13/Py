import datetime

class DateTimeValue:
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.value = datetime.datetime(year, month, day, hour, minute, second)

    def __str__(self):
        return self.value.strftime('%Y-%m-%d %H:%M:%S')

# Пример использования
date_time = DateTimeValue(2022, 12, 31, 23, 59, 59)
print(date_time)  # Выводит: 2022-12-31 23:59:59
