recorded_values = [48,47,54,50,42,68,39,46]

too_high_values = list(filter(lambda x:x>50, recorded_values))

print("Too high:",",".join(map(lambda x:str(x), too_high_values)))