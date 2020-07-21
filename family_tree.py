my_family = {
    "mom": {
        "name": "Serah",
        "age": "'21'"
    },
    "dad": {
        "name": "Steven",
        "age": "42"
    },
    "oldest sister": {
        "name": "Zoey",
        "age": "11"
    },
    "middle sister": {
        "name": "Lucy",
        "age": "5"
    },
    "youngest sister": {
        "name": "Amelia",
        "age": "3"
    }
}

for fam, info in my_family.items():
    print(f'{info["name"]} is my {fam} and is {info["age"]} years old.')