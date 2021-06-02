family_age = {
  "Marta": 30,
  "Basia": 3,
  "Wanda": 0,
}

print(family_age["Marta"])
family_age["Antoni"] = 0

print(family_age)

family = (
  {"name": "Marta", "age": 30},
  {"name": "Basia", "age": 30},
  {"name": "Wanda", "age": 30},
)

print(family[0]["name"])
print(family[1]["name"])
print(family[2]["name"])

list_family = [
  ("Marta", 30),
  ("Basia", 30),
  ("Wanda", 30),
]

dict_family = dict(list_family)

print(list_family)
print(dict_family)