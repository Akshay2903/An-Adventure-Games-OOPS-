# from character import Character

# dave = Character("Dave","A smelly zombie")
# dave.describe()


# dave.set_conversation ("Hello, how are you? what's going on.") 
# dave.talk()


# michael=Character ("Michael", "An ugly big fellow") 
# michael.describe ()

# michael.set_conversation(None)
# michael.talk()

# michael.fight ("I")

from character import Enemy

dave = Enemy("dave","A smeely zombie")
dave.describe()

dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)


