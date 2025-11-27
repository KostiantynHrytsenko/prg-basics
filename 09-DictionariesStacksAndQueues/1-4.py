person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])

person["surname"] = "Nowak"
if(person["married"]):
    person["married"] = False
else:
    person["married"] = True

print(person)