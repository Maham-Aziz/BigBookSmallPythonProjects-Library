### BBSMP- Bagels.py
### Project 1
### Maham Aziz
### Januray 26, 2024

print("I am thinking of a 3-digit number between 100 and 999. Try to guess what it is.")
print("Here are some clues:")
print("When I say:     That means:")
print("  Pico          One digit is correct but in the wrong position.")
print("  Fermi         One digit is correct and in the right position.")
print("  Bagels        No digit is correct")

print("I have thought up a number. You have 10 guesses to get it.")
print()

import random

numb = random.randrange(100,1000)
numb = str(numb)
print()

guess_count = 0
while guess_count <= 9:
    final = []
    n_list = []
    g_list = []
    guess = input("Please enter you number guess: ")
    if guess == numb:
        print("You got it!")
        repeat = input("Do you want to play again? (yes or no)")
        if repeat == 'yes':
            guess_count = 0
            continue
        else:
            exit()
    else:
        for x in numb:
            n_list.append(x)
        for y in guess:
            g_list.append(y)
        if n_list[0] in g_list:
            if n_list[0] == g_list[0]:
                final.append("Fermi")
            else:
                final.append("Pico")
        if n_list[1] in g_list:
            if n_list[1] == g_list[1]:
                final.append("Fermi")
            else:
                final.append("Pico")
        if n_list[2] in g_list:
            if n_list[2] == g_list[2]:
                final.append("Fermi")
            else:
                final.append("Pico")
    if final == []:
        final.append("Bagels")

    print(final)
    guess_count +=1
