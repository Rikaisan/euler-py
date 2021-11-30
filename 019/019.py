from collections import Counter

day_names = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

leap_years = [year for year in range(1900, 2001) if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)]

day = 0  # 0 - Monday, 6 - Sunday
first_days = []
for year in range(1900, 2001):
    for month in range(1, 13):
        first_days.append(day_names[day])
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = (day + 3) % 7
        elif month in (4, 6, 9, 11):
            day = (day + 2) % 7
        if year in leap_years and month == 2:
            day = (day + 1) % 7

first_days = first_days[12:]  # Removes 1900 from the list
print(Counter(first_days))
