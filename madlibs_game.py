# Code by amotef@gmail.com

# Mad Libs Game

# Mad Libs is a phrasal template word game.

# Example:
# We start with a story, containing several blanked out words. Here’s a basic example:
# Rumble in the  _______.
# We then prompt the user to fill in the gaps, in this case, with a noun or place. We might end up with something like this:
# Rumble in the Toilet.


# Solution 1 - simple

food = input("Enter a type of food: ")
girl = input("Enter a girl's name: ")
adj1 = input("Enter an adjective: ")
bird = input("Enter a noun: ")
verb1 = input("Enter a verb in the past tense: ")
verb2 = input("Enter another verb in the past tense: ")
verb3 = input("Enter a third verb in the past tense: ")
noun1 = input("Enter a noun: ")
story = "It was " + food + " day at school, and " + jamie + " was super " + adj1 + " for lunch. But when she went outside to eat, a " + bird + " stole her " + food + "! " + jamie + " chased the " + bird + " all over school. She " + verb1 + ", " + verb2 + ", and " + verb3 + " through the playground. Then she tripped on her " + noun1 + " and the " + bird + " escaped! Luckily, " + jamie + "'s friends were willing to share their " + food + " with her."
 
print(story)

