dog_age_1 = 15
dog_age_2 = 24

dog_age = int(input("Input dog's age: ")) # Do not change this line
human_age = 0


if 0 < dog_age < 17:
    if dog_age == 1:
        human_age = dog_age_1
    elif dog_age == 2:
        human_age = dog_age_2
    else:
        human_age = dog_age_2 + 4*(dog_age-2)
    print("Human age: ", human_age)
else:
    print("Invalid age")