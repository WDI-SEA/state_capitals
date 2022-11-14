import random
states = [
    {
        "name": "Alabama",
        "capital": "Montgomery"
    }, {
        "name": "Alaska",
        "capital": "Juneau"
    }, {
        "name": "Arizona",
        "capital": "Phoenix"
    }, {
        "name": "Arkansas",
        "capital": "Little Rock"
    }, {
        "name": "California",
        "capital": "Sacramento"
    }, {
        "name": "Colorado",
        "capital": "Denver"
    }, {
        "name": "Connecticut",
        "capital": "Hartford"
    }, {
        "name": "Delaware",
        "capital": "Dover"
    }, {
        "name": "Florida",
        "capital": "Tallahassee"
    }, {
        "name": "Georgia",
        "capital": "Atlanta"
    }, {
        "name": "Hawaii",
        "capital": "Honolulu"
    }, {
        "name": "Idaho",
        "capital": "Boise"
    }, {
        "name": "Illinois",
        "capital": "Springfield"
    }, {
        "name": "Indiana",
        "capital": "Indianapolis"
    }, {
        "name": "Iowa",
        "capital": "Des Moines"
    }, {
        "name": "Kansas",
        "capital": "Topeka"
    }, {
        "name": "Kentucky",
        "capital": "Frankfort"
    }, {
        "name": "Louisiana",
        "capital": "Baton Rouge"
    }, {
        "name": "Maine",
        "capital": "Augusta"
    }, {
        "name": "Maryland",
        "capital": "Annapolis"
    }, {
        "name": "Massachusetts",
        "capital": "Boston"
    }, {
        "name": "Michigan",
        "capital": "Lansing"
    }, {
        "name": "Minnesota",
        "capital": "St. Paul"
    }, {
        "name": "Mississippi",
        "capital": "Jackson"
    }, {
        "name": "Missouri",
        "capital": "Jefferson City"
    }, {
        "name": "Montana",
        "capital": "Helena"
    }, {
        "name": "Nebraska",
        "capital": "Lincoln"
    }, {
        "name": "Nevada",
        "capital": "Carson City"
    }, {
        "name": "New Hampshire",
        "capital": "Concord"
    }, {
        "name": "New Jersey",
        "capital": "Trenton"
    }, {
        "name": "New Mexico",
        "capital": "Santa Fe"
    }, {
        "name": "New York",
        "capital": "Albany"
    }, {
        "name": "North Carolina",
        "capital": "Raleigh"
    }, {
        "name": "North Dakota",
        "capital": "Bismarck"
    }, {
        "name": "Ohio",
        "capital": "Columbus"
    }, {
        "name": "Oklahoma",
        "capital": "Oklahoma City"
    }, {
        "name": "Oregon",
        "capital": "Salem"
    }, {
        "name": "Pennsylvania",
        "capital": "Harrisburg"
    }, {
        "name": "Rhode Island",
        "capital": "Providence"
    }, {
        "name": "South Carolina",
        "capital": "Columbia"
    }, {
        "name": "South Dakota",
        "capital": "Pierre"
    }, {
        "name": "Tennessee",
        "capital": "Nashville"
    }, {
        "name": "Texas",
        "capital": "Austin"
    }, {
        "name": "Utah",
        "capital": "Salt Lake City"
    }, {
        "name": "Vermont",
        "capital": "Montpelier"
    }, {
        "name": "Virginia",
        "capital": "Richmond"
    }, {
        "name": "Washington",
        "capital": "Olympia"
    }, {
        "name": "West Virginia",
        "capital": "Charleston"
    }, {
        "name": "Wisconsin",
        "capital": "Madison"
    }, {
        "name": "Wyoming",
        "capital": "Cheyenne"
    }]




# test_states = [
#     {
#         "name": "Arkansas",
#         "capital": "Little Rock"
#     }, {
#         "name": "California",
#         "capital": "Sacramento"
#     }, {
#         "name": "Colorado",
#         "capital": "Denver"
#     }]








def game():
    n = 1
    # *Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.
    random_states = random.sample(states, len(states))
   # *Initialize new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times the answer is wrong.
    game_score = {}
    game_score['right'] = 0
    game_score['wrong'] = 0
    while  n < len(random_states):
        # *Provide a welcome message to introduce the player to the game.
        print(" Welcome to the State Capital game! Are you smarter than a 3rd grader?\n We will give you a state, you will have to guess the capital.\n Remember spelling and capitalization matter!")
        # *Through all 50 states, prompt the user to name the capital of the state.
        for item in random_states:
            q = input(f" Q.{n} What is the capital of " + item["name"] + "?")
        # *If the answer is correct, display a message saying so, and increment the correct key.
            if q == item["capital"]:
                n += 1
                game_score["right"] += 1
                print(
                    f" Good job 😍!\n You have {game_score['right']} correct and {game_score['wrong']} wrong")
        # *If the answer is wrong, display a message saying so, and increment the wrong key.
            else:
                n += 1
                game_score["wrong"] += 1
                print(
                    f" Better luck next time 😭!\n You have {game_score['right']} correct and {game_score['wrong']} wrong")
    # *Once the user has gone through all 50 states, ask them if they'd like to play again.
    play_again = input(f" You reached the end!\n Your score is {game_score['right']} correct and {game_score['wrong']} wrong. Do you want to play again? yes or no ")
    if play_again == 'yes':
        random_states = random.sample(states, len(states))
        n = 1
        game_score['right'] = 0
        game_score['wrong'] = 0
        game()
    elif play_again == 'no':
        print("Thanks for playing!")

game()


# Bonus! Calculate a overall total score, display a running tally for each prompt If the user plays again, set the order of how the prompts appear to start with the ones they got wrong the most often. Add a hint functionality that prints the first 3 letters of a capital
