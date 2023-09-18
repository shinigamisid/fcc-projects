def add_time(start, duration, Day_of_the_week_Input = False):
    converted_hours = 0
    start_separate_by_space = start.split()
    start_HM = start_separate_by_space[0].split(':')
    start_hours = start_HM[0]
    start_minutes = start_HM[1]
    duration_split = duration.split(':')
    duration_hours = duration_split[0]
    duration_minutes = duration_split[1]
    new_time = ''
    am_pm = start_separate_by_space[1]
    if am_pm == 'PM':
        converted_hours = int(start_hours) + 12
        result_hours = converted_hours + int(duration_hours)
        result_minutes = int(start_minutes) + int(duration_minutes)
        if result_minutes > 59:
            result_hours = result_hours + 1
            result_minutes = result_minutes - 60
        hours = (result_hours-12) % 12
        if hours == 0: hours = 12
        if result_hours > 12:
            if result_hours >= 24:
                if result_hours >= 48:
                    a = (int(duration_hours) // 24) + 1
                    new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " AM" + f" ({a} days later)"
                else:
                    new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " PM" + " (next day)"
            else:
                new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " PM"
        else:
                new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " PM"
    else:
        converted_hours = int(start_hours)
        result_hours = converted_hours + int(duration_hours)
        result_minutes = int(start_minutes) + int(duration_minutes)
        if result_minutes > 59:
            result_hours = result_hours + 1
            result_minutes = result_minutes - 60
        hours = (result_hours-12) % 12
        if hours == 0: hours = 12
        if result_hours > 12:
            if result_hours >= 24:
                if result_hours >= 48:
                    a = (int(duration_hours) // 24) + 1
                    new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " PM" + f" ({a} days later)"
                else:
                    new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " AM" + " (next day)"
            else:
                new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " AM"
        else:
            new_time = str(hours) + ":" + str(result_minutes).rjust(2, '0') + " AM"

    return new_time