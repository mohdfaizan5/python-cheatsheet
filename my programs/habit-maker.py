print("THE HABIT MAKER\n")
habit = input("What is the habit:\n")
cue = input(" What reminds you to start that habit\n")
craving = input(" What can make this habit so attractive")
response = input(" How can I make it easy")
reward = input("Plan a reward everytime you do this, so that your motivated to do next time")

final = (f"""I want to build this {habit} habit, for this I will {cue}, 
by this i get {craving}, for doing this daily i'll {response}, when i do this i get {reward}
""")

print(final)
