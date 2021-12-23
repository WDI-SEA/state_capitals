from capitals import states
import random
import pprint 


total_answered = 0

def main():
    game_setup()
    play()
    
def game_setup():
    # Randomize Order of States...
    random.shuffle(states)

    # Insert New Keys and Values for Right and Wrong Answers...
    for entries in states:
        entries["right"] = 0
        entries["wrong"] = 0
        entries["answered"] = False


def play():
    # Need to declare a global to use a variable outside of local scope? WTF!!!!!
    global total_answered
    global continue_play
    while continue_play == "Y":
        for entries in states:
            if entries["answered"] == True:
                continue
            else:
                print(f'What is the capital of {entries["name"]}: \n')
                answer = input("> ")
                print(f"You typed: {answer} \n\n")

                if answer.lower() == entries["capital"].lower():
                    entries["right"] += 1
                    entries["answered"] = True;
                    total_answered += 1
                    print("Your answer as correct! \n")
                    print(f"So far, you've answered {entries['right']} out of {total_answered} questions correctly. \n")

                else: 
                    print("Your answer was incorrect...\n")
                    entries["wrong"] += 1
                    entries["answered"] = True;
                    total_answered += 1
                    print(f"So far, you've answered {entries['wrong']} out of {total_answered} questions incorrectly. \n")

            print(f"{entries}\n")
        
        if total_answered == 50:
            print("Do you want to play again? \n")
            continue_play = input("Press Y or N \n")

            if play_again == "Y":
                for entries in states:
                    entries["answered"] == False
                    total_answered = 0
                    random.shuffle(states)
                    # Hmm..how do I "replay" without calling play() inside of play()
            else:
                exit()


# PseudoCode:
#
continue_play = "Y"
total_answered = 0
main()







pprint.pprint(states)

# States should not appear in Alphabetical Order



