import random

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')

#Variable Initialization
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
hangman_pics = [
''' ________________
    |/      
    |      
    |     
    |       
    |      
    |
____|___''',
''' ________________
    |/      |
    |      (_)
    |      
    |       
    |      
    |
____|___''',
''' __________
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
____|___''',
''' __________
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
____|___''',
''' __________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
____|___''',
''' __________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
____|___''',
''' __________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
____|___''',
]
random_word = list(random.choice(words))
len_ran_word = len(random_word)
blank=[]
flag=0
turn = 0

def list_to_string(blank):
    str=""
    for letter in blank:
        str+=letter
    return str

#Initial Blank Space Print
for letter in range(0,len_ran_word):
    print("_ ",end=" ")
print(" ")

for letter in range(0,len_ran_word):
    blank.append("_ ")

while turn<len(hangman_pics):
    guess = input("Enter your guess: ").lower()

    for letter in range(0, len_ran_word):
        if blank[letter].strip() == guess:
            if turn == 6:
                print(hangman_pics[turn])
                print("GAME OVER. The man was hanged. :(")
            else:
                print("Sorry, letter already guessed. You have "+str(6-turn)+" tries left.")
                print(hangman_pics[turn])
                turn+=1
                break

    for letter in range(0,len_ran_word):
        if random_word[letter].strip() == guess:
            blank[letter] = guess+" "
        else:
            continue

    for letter in range(0,len_ran_word):
        if blank[letter].strip() == guess:
            flag = 1

    if flag == 1:
        print("\n"+list_to_string(blank).upper())
    else:
        if turn == 6:
            print(hangman_pics[turn])
            print("GAME OVER. The man was hanged. :(")
        else:
            print("Sorry, wrong choice. You have "+str(6-turn)+" tries left.")
            print(hangman_pics[turn])

        if not turn == 6:
            print("\n"+list_to_string(blank).upper())
        turn += 1
    flag = 0

    if list_to_string(blank).replace(" ","") == list_to_string(random_word):
        print("Thank You! You saved the man's life. :)")
        break