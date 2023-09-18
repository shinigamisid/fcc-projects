
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def time_to_int(time):
    """
    Converts string time to list that allows calculation.
    :param time: string like "3:00 PM"
    :return: [int, int, str] like [3, 0, 'PM']
    """
    ampm_separated = time.split()
    int_time = ampm_separated[0].split(":")
    if len(ampm_separated) > 1:  # accounting for duration splitting where there is no 'AM' or 'PM'
        int_time.append(ampm_separated[1])
        int_time[0] = int(int_time[0])
        int_time[1] = int(int_time[1])
    else:
        int_time[0] = int(int_time[0])
        int_time[1] = int(int_time[1])
    return int_time


def time_addition(start_time, duration_to_add):
    """
    Adds duration to a starting time.
    :param start_time: time string "7:31 AM"
    :param duration_to_add: duration string "3:00"
    :return: [10, 31, 'AM'] (does NOT convert 'AM' to 'PM' or 'PM' to 'AM')
    """
    day_count = 0
    start_time = time_to_int(start_time)
    duration_to_add = time_to_int(duration_to_add)
    hrs_after_add = start_time[0] + duration_to_add[0]
    min_after_add = start_time[1] + duration_to_add[1]
    time_after_add = [hrs_after_add, min_after_add, start_time[2]]
    while time_after_add[0] > 23:
        day_count += 1
        time_after_add[0] -= 24
    if start_time[2] == "PM" and time_after_add[0] > 12:
        day_count += 1
    time_after_add.append(day_count)
    return time_after_add


def ampm_convert(input_time):
    """
    Converts AM to PM/PM to AM if needed.
    :param input_time: example [14, 90, "PM", 1]
    :return: [3, 30, "AM", 1]
    """
    answer_time = input_time
    if input_time[3] == 1:
        answer_time[2] = "AM"
        answer_time[0] -= 12
    if input_time[1] > 59:
        answer_time[0] += 1
        answer_time[1] -= 60
    if input_time[2] == "AM" and input_time[0] > 11:
        answer_time[2] = "PM"
        answer_time[0] -= 12
    if input_time[2] == "PM" and input_time[0] > 12:
        answer_time[2] = "AM"
        answer_time[0] -= 12
    if answer_time[0] == 0:
        answer_time[0] = 12
    return answer_time


def day_calculator(time_conv, starting_day):
    """

    :param time_conv:
    :param starting_day:
    :return:
    """
    starting_day = starting_day.capitalize()
    starting_day = (days_of_week.index(starting_day) + time_conv[3]) % len(days_of_week)
    return days_of_week[starting_day]


def add_time(start, duration, starting_day=''):
    starting_day = starting_day.casefold()
    added_time = time_addition(start, duration)
    calculated_time = ampm_convert(added_time)
    if calculated_time[3] > 1:
        if starting_day == '':
            calculated_time[0] = f"{calculated_time[0]}"
            calculated_time[1] = f"{calculated_time[1]:0>2}"
            new_time = f"{calculated_time[0]}:{calculated_time[1]} {calculated_time[2]} ({calculated_time[3]} days later)"
        else:
            changed_day = day_calculator(calculated_time, starting_day)
            calculated_time.append(changed_day)
            calculated_time[0] = f"{calculated_time[0]}"
            calculated_time[1] = f"{calculated_time[1]:0>2}"
            new_time = f"{calculated_time[0]}:{calculated_time[1]} {calculated_time[2]}, {calculated_time[4]} ({calculated_time[3]} days later)"
    elif calculated_time[3] == 1:
        if starting_day == '':
            calculated_time[0] = f"{calculated_time[0]}"
            calculated_time[1] = f"{calculated_time[1]:0>2}"
            new_time = f"{calculated_time[0]}:{calculated_time[1]} {calculated_time[2]} (next day)"
        else:
            changed_day = day_calculator(calculated_time, starting_day)
            calculated_time.append(changed_day)
            calculated_time[0] = f"{calculated_time[0]}"
            calculated_time[1] = f"{calculated_time[1]:0>2}"
            new_time = f"{calculated_time[0]}:{calculated_time[1]} {calculated_time[2]}, {calculated_time[4]} (next day)"
    else:
        if starting_day == '':
            calculated_time[0] = f"{calculated_time[0]}"
            calculated_time[1] = f"{calculated_time[1]:0>2}"
            new_time = f"{calculated_time[0]}:{calculated_time[1]} {calculated_time[2]}"
        else:
            changed_day = day_calculator(calculated_time, starting_day)
            calculated_time.append(changed_day)
            calculated_time[0] = f"{calculated_time[0]}"
            calculated_time[1] = f"{calculated_time[1]:0>2}"
            new_time = f"{calculated_time[0]}:{calculated_time[1]} {calculated_time[2]}, {calculated_time[4]}"
    return new_time


print(add_time("2:59 AM", "24:00", "saturDay"))
