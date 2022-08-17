import random


# create a welcome message
# randomize the dictionary

# Initialize new keys in the dictionaries that store the number
# loop through all 50 states 
# if input = correct display correct 
# if input = correct, increment the new "correct key"
# if input = incorrect display incorrect 
# if input = incorrect, increment the new "incorrect key"
# after player gets through all 50 states adisplay message should    appear asking if they'd lide to play again 
#




# test_states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }
# ]










# for state in testStates:
#     print(state)
# random.shuffle(testStates)
# print(testStates[1], "capital")

# for key, value in testStates.items():
#     print('key', key)
#     print('value', value)

# correct = [ state for state in states if ]











test_states = [
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

for test_state in test_states:
    test_state["right"] = 0
    test_state["wrong"] = 0


print("Lets play the State Capital Game, dont forget answers are case sensitive!\n")
play_game = True
while (play_game):
    correct_answer = 0
    incorrect_answer = 0
    random.shuffle(test_states)
    for test_state in test_states:
        answer = input(f"what is the capital of {test_state['name']}?\n")
        if answer == test_state["capital"]:
            test_state["right"] += 1
            correct_answer += 1
            print("correct, Great Job")
        else: 
            test_state["wrong"] += 1
            incorrect_answer += 1
            print("sorry charlie, that is incorrect")
        print(f"Correct Answers: {correct_answer} ; Incorrect Answers: {incorrect_answer}")
        print(f"Correct answers for this state: {test_state['right']} out of {correct_answer + incorrect_answer}" )
    play_again = input("thats all 50 states, do you want to play again (y/n)\n")
    if play_again == "n":
        play_game = False
        print("Nice job, see ya soon")