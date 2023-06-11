# looks exactly like json but it's a dictionary
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne",
    "Spiderman": "Peter Parker",
}

# another way to define a dictionary
"""heroes_dictionary = dict([
        ("Superman", "Clark Kent"),
        ("Batman", "Bruce Wayne"),
        ("Spiderman"), ("Peter Parker")
    ]
)"""  # idk why this resulted in error

print("Length: ", len(heroes))
print(heroes["Superman"])
heroes["Flash"] = "Barry Allan"  # woops a typo
heroes["Flash"] = "Barry Allen"  # fixed the typo

print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))

# delete a key
del heroes["Flash"]
print(heroes.pop("Batman"))
print("Superman" in heroes)

for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

# dictionary mapping
dic = {"name": "Bread", "price": 2.99}
print("%(name)s costs %(price).2f" % dic)
