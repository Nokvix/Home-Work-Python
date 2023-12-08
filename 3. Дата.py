class Date:
    @classmethod
    def from_string(cls, date: str) -> str:
        day, month, year = date.split("-")
        return f"День: {day}\tМесяц: {month}\tГод: {year}"

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split("-"))
        return 0 < int(day) < 13 and 0 < int(month) < 13 and 1000 < int(year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
