DAYS_IN_YEAR = 365
DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

SECONDS_IN_DAY = 86400  # 60*60*24
SECONDS_IN_HOUR = 3600  # 60*60
SECONDS_IN_MINUTE = 60

with open('task1.txt') as f:
    born_date = f.readline().split()
    death_date = f.readline().split()


born_date = list(map(int, born_date))    # list[str] -> list[int]
death_date = list(map(int, death_date))  # list[str] -> list[int]


def count_seconds(date): # считаю сколько секунд прошло с 0 года 0 месяца 0 дня 0:0:0
    date_seconds = date[0] * DAYS_IN_YEAR * SECONDS_IN_DAY

    seconds_in_month = [days_in_month * SECONDS_IN_DAY for days_in_month in DAYS_IN_MONTHS]
    for month_number in range(date[1] - 1):
        date_seconds += seconds_in_month[month_number]

    date_seconds += date[2] * SECONDS_IN_DAY
    date_seconds += date[3] * SECONDS_IN_HOUR
    date_seconds += date[4] * SECONDS_IN_MINUTE
    date_seconds += date[5]

    return date_seconds


born_date_seconds = count_seconds(born_date)
death_date_seconds = count_seconds(death_date)

diff_seconds = death_date_seconds - born_date_seconds   # прошло секунд с роджения до смерти

days = diff_seconds//SECONDS_IN_DAY     # дней с роджения до смерти (целочисленно делю на SECONDS_IN_DAY)
seconds = diff_seconds%SECONDS_IN_DAY   # секунд с роджения до смерти без дней (остаток от деления на SECONDS_IN_DAY)
print(days, seconds)
