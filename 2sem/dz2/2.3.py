def add_friends(nameOfPerson, listOfperson):
    name = []
    for i in listOfperson:
        name.append(i)
    a = friends.get(nameOfPerson, 1)
    if a != 1:
        for i in friends[nameOfPerson]:
            name.append(i)
    friends[nameOfPerson] = name

def is_friends(nameOfPerson1, nameOfPerson2):
    if nameOfPerson2 in friends[nameOfPerson1]:
        return True
    else:
        return False


def print_friends(nameOfPerson):
    print(friends[nameOfPerson])


friends = dict()


add_friends("Алла", ["Марина", "Иван"])

print(is_friends("Алла", "Мария"))

add_friends("Алла", ["Мария"])

print(is_friends("Алла", "Мария"))