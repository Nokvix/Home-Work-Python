class Date:
    @staticmethod
    def from_string(date: str) -> str:
        day, month, year = date.split("-")
        return f"День: {day}    Месяц: {month}    Год: {year}"

    @staticmethod
    def is_date_valid(date: str) -> bool:
        day, month, year = date.split("-")
        return 0 < int(day) < 13 and 0 < int(month) < 13 and 1000 < int(year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
