people = [
    {'name':'John','age':24},
    {'name':'Ann','age':19},
    {'name':'Peter','age':31}
]

print(people)

people_sorted= sorted(people, key=lambda x:x["age"], reverse=True)

print(people_sorted)