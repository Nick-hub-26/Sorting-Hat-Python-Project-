import random

print('===============')
print('The Sorting Hat')
print('===============')

print("\n\nThe Sorting hat will now ask you 3 questions to determine which house you belong to. Are you ready?\n")
while True:
    start = input("Type yes or no: ")
    if start == "yes" or start == "Yes":
        print("Great! Let the quiz commence\n")
        break
    elif start == "no" or start == "No":
        print("\nNo problem, come back when you're ready. Goodbye!")
        exit()
    else:
        print("\n--INVALID INPUT--\n")
        print("Try again:")
        continue
houses = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

# Question 1
while True:
    print("""Do you like Dawn or Dusk?
    1. Dawn
    2. Dusk""")
    q1 = input("\nEnter your answer 1-2: ")

    if q1 == "1":
        houses["Gryffindor"] += 1
        houses["Ravenclaw"] += 1
        break
    elif q1 == "2":
        houses["Hufflepuff"] += 1
        houses["Slytherin"] += 1
        break
    else:
        print("\n--INVALID INPUT--\n")
        print("Try again:")
        continue
    
# Question 2
while True:
    print("""\nWhen I'm dead, I want people to remember me as:
    1. The Good
    2. The Great
    3. The Wise
    4. The Bold""")
    q2 = input("Enter your answer 1-4: ")

    if q2 == "1":
        houses["Hufflepuff"] += 1
        break
    elif q2 == "2":
        houses["Slytherin"] += 1
        break
    elif q2 == "3":
        houses["Ravenclaw"] += 1
        break
    elif q2 == "4":
        houses["Gryffindor"] += 1
        break
    else:
        print("--\nINVALID INPUT--\n")
        print("Try again:")
        continue

# Question 3
while True:
    print("""\nWhich kind of instrument most pleases your ear?:
    1. The violin
    2. The trumpet
    3. The piano
    4. The drum""")
    q3 = input("Enter your answer 1-4: ")

    if q3 == "1":
        houses["Slytherin"] += 1
        break
    elif q3 == "2":
        houses["Hufflepuff"] += 1
        break
    elif q3 == "3":
        houses["Ravenclaw"] += 1
        break
    elif q3 == "4":
        houses["Gryffindor"] += 1
        break
    else:
        print("--\nINVALID INPUT--\n")
        print("Try again:")
        continue


# Determine the house with the highest score
top_score = max(houses.values())

# Collect all houes that share the top score
winners = [house for house, score in houses.items() if score == top_score]

# Pick randomly from the winners if there is a tie
result = random.choice(winners)

print(f"\nThe Sorting Hat has chosen... Your house is {result}!")
