from cat import Cat

cats = [
    {
     "name": 'Барон',
     "gender": 'мальчик',
     "age": 2,
    },
    {
        "name": 'Сэм',
        "gender": 'мальчик',
        "age": 2,
    },
]

for cat in cats:
    pet = Cat(name = cat.get('name'), gender = cat.get('gender'), age = cat.get('age'))
    pet.print()