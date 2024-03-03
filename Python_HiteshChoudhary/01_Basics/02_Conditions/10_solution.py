#-------------------------------------------------------------------------------#
#                         10. Pet Food Recommendation
#-------------------------------------------------------------------------------#
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter pet 1.Dog 2.Cat: ").lower()

if pet == "dog":
    age = int(input("How old your pet is: "))
    if age < 2:
        food = "Puppy Food"
    else:
        food = "Senior Dog Food"
elif pet == "cat":
    age = int(input("How old your pet is: "))
    if age < 5:
        food = "Kitty Food"
    else:
        food = "Senior Cat Food"
else:
    print("currently we have info about Dog and Cat other pet info will be added soon")
    exit()

print("Food for your ", pet, "is", food)