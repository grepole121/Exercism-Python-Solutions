from calendar import Calendar
import datetime


def meetup(year, month, week, day_of_week):

    possible_dates = []
    for date in Calendar().itermonthdates(year, month):
        if date.month == month and date.strftime('%A') == day_of_week:
            possible_dates.append(date)

    if week == "last":
        return possible_dates[-1]
    elif week == "teenth":
        for date in possible_dates:
            if 13 <= date.day <= 19:
                return date
    else:
        week_pos = int(week[0]) - 1
        try:
            return possible_dates[week_pos]
        except:
            raise MeetupDayException("ERROR")


class MeetupDayException(ValueError):
    pass
