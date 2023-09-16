import random

print("What do you want do say to de magic 8 ball?")
question = input()

positive_anwsers = ["Absolutely","Of course","Your chances are high","Go deep into it","You will get it","Possibly","I hope so","Yes","I predict a positive future","Yes, you will"]
normal_anwsers = ["Maybe", "I don't know", "I can't answer you now", "Ask for some other ball", "50/50" ]
negative_anwsers = ["No", "Absolutely not", "Your chances are low", "I hope so", "Never"]


List = random.randint(1,3)

if List == 1:
    ball = positive_anwsers
elif List == 2:
    ball = normal_anwsers
else:
    ball = negative_anwsers

final_anwser = random.choice(ball)

print()
print("The magic 8 ball says:",final_anwser)