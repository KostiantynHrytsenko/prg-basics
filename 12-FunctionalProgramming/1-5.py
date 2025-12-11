def avg_speed(distance, hours, minutes):
    result = distance / (hours + minutes/60)
    return result

print(avg_speed(70, 1, 23))