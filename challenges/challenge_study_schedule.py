def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0
    for time in permanence_period:
        try:
            if time[0] <= target_time <= time[1]:
                counter += 1
        except TypeError:
            return None
    return counter
