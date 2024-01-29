### BBSMP- bagels.py
### project #1
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
print(numb)
print()

guess_count = 0
sim_count = 0
aa = 0
while guess_count <= 10:
    guess = input("Please enter you number guess: ")
    if guess == numb:
        print("You got it!")
        repeat = input("Do you want to play again? (yes or no)")
        if repeat == 'yes':
            continue
        else:
            exit()
    else:
        for x in numb:
            print(x)
            if x in guess:
                aa += 1
                print(aa + 101)
                if aa == 1:
                    index1 = numb.index(x)
                    index2 = guess.index(x)
                    if index1 == index2:
                        print("Fermi")
                    else:
                        print("Pico")
                else:
                    print("Bagels")
            else:
                print("Bagels")
    guess_count += 1    
                
            #else:
                #print("")
            #str_guess = str(guess)
            #find = str_guess.count(x)
            #if find == 1:
            #    str(numb)
            #    find_numb = numb.find(x)
            #    find_guess = guess.find(x)
            #    if find_numb == find_guess:
            #        print("Fermi")
            #    else:
            #        print("Pico")
            #elif find == 0:
            #    print("Bagels")
   # guess_count += 1

                
                
