import json

#f variable assigned to pass me-capitals.json contents with 'open' built-in function/ 
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    # print(data)

total = len(data["cards"])
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess.lower() == i["a"].lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")