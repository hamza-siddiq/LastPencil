def next_(name):
    return person1 if name == person2 else person2


def numeric_check(pencils):
    while not pencils.isnumeric() or int(pencils) < 0:
        pencils = input("The number of pencils should be numeric\nPossible values: '1', '2', '3' or more if choosing a number")
        pencils = positivity_check(pencils)
    return int(pencils)


def positivity_check(pencils):
    while pencils == 0:
        pencils = input("The number of pencils should be positive\nPossible values: '1', '2', '3'")
        pencils = numeric_check(pencils)
    return pencils


def pick_number():
    number = input("How many pencils would you like to use:")
    number = numeric_check(number)
    number = positivity_check(number)
    return int(number)


def pick_pencils(person):
    pencils = input(f"{person}'s turn:")
    pencils = numeric_check(pencils)
    pencils = positivity_check(pencils)
    while pencils > 3 or pencils < 1:
        pencils = input("Possible values: '1', '2' or '3'")
        pencils = numeric_check(pencils)
        pencils = positivity_check(pencils)
    while pencils > total_pencils:
        pencils = input("Too many pencils were taken")
        pencils = numeric_check(pencils)
        pencils = positivity_check(pencils)
    return int(pencils)


def pick_person(name1, name2):
    name = input(f"Who will be the first ({name1}, {name2}):")
    while name != name1 and name != name2:
        name = input(f"Choose between '{name1}' and '{name2}':")
    return name


def winning_strategy_bot(pencils, person):
    print(f"{person}'s turn:")
    if pencils % 4 == 0:
        print(3)
        return 3
    if pencils % 4 == 3:
        print(2)
        return 2
    if pencils % 4 == 2:
        print(1)
        return 1
    if pencils % 4 == 1:
        print(1)
        return 1


total_pencils = pick_number()
person1 = "John"
person2 = "Jack"
person = pick_person(person1, person2)

while total_pencils > 0:
    print("|" * total_pencils)
    if person == person1:
        turn_pencils = pick_pencils(person)
    elif person == person2:
        turn_pencils = winning_strategy_bot(total_pencils, person)
    total_pencils -= turn_pencils
    person = next_(person)

print(f"{person} won!")