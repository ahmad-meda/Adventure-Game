import random
import time

name = input("Please enter your name \n-->")


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for option in options:
            if option == response:
                return response
        print_pause("pls try again")


def start():
    print_pause("You get bored of your daily life and start wishing for a "
                "life threatening adventure.")
    print_pause("Suddenly you find youself in front of 3 doors.."
                "and holding an adventure kit..")
    print_pause("A real life adventure!!..you think to yourself..")
    print_pause("A board reads,'WELCOME TO THE COLOSSAL LABYRINTH!!',"
                "triumph and earn unfathomable treasures..")
    print_pause(
        "Lose and you shall taste despair!..The moment of victory shall be"
        "achieved when you obtain the legendary blade of dragon glass!!")
    print_pause("There are three doors in front of you,"
                "one on your left and right and one in front of yourself..")
    print_pause("which one do you take?")

    choice = valid_input("Answer Left,Right or Forward \n-->",
                         ["left", "right", "forward"])
    if "left" in choice:
        dragon_room()
    elif "right" in choice:
        pot_of_gold()
    else:
        shady_kitchen()


def dragon_room():
    print_pause("You hear a deafening roar as you open the door "
                "and see a monstrous dragon!")
    print_pause("You panic and look through your kit and find a "
                "flamethrower and an excalibur.. ")
    # chances = 1
    # while True and chances <= 2:
    weapon = valid_input("You have to kill the dragon in one shot,"
                         "what do you choose?\n -->",
                         ["flamethrower", "excalibur"])
    if "flame" in weapon:
        print_pause("You amazingly hit the bullseye and"
                    " annhilate the dragon completely!")
        print_pause("You are rewarded with the map of the labyrinth.")
        question(
            "I speak without a mouth and hear without ears. "
            "I have no body, but I come alive with wind. What am I?\n--->",
            "echo")
        # break
    elif "exc" in weapon:
        print_pause("You swing the sword around like a clumsy idiot"
                    "and lose your arm..sadge")
        print_pause("But you manage to kill the dragon somehow,lucky yoy :/ .")
        question(
            "I speak without a mouth and hear without ears. I have no body, "
            "but I come alive with wind. What am I?\n--->",
            "echo")
        # break
    else:
        # if chances == 1:
        # print_pause('Seems like your brain got fried,pls try again')
        # chances += 1
        print_pause("You drown in your own pool of stupidity and "
                    "the dragon eats you alive and you die.nice try:^{")


def pot_of_gold():
    print_pause("You open the door and see a pot of gold that "
                "looks like a miniature sun")
    print_pause("Knowing its too good to be true to not be a trap,"
                "u debate whether to take the pot or a portion of it.")
    amount = valid_input("Do u empty the pot or do you take a portion? "
                         "\n--->", ["portion", "empty"])
    if "portion" in amount:
        print_pause("Caution pays off and u gain a mythical grade dagger.")
        question("You measure my life in hours and I serve you by expiring. "
                 "I’m quick when I’m thin and slow when I’m fat."
                 "The wind is my enemy.What am I?\n--->", "candle")
    elif "empty" in amount:
        print_pause(
            "Your greediness causes your downfall as you find a snake in "
            "the bottom and get stung paralyzing half your body")
        question("You measure my life in hours and I serve you by expiring."
                 "I’m quick when I’m thin and slow when I’m fat. "
                 "The wind is my enemy.What am I?\n--->", "candle")
    else:
        print_pause("Your low IQ jello brain evaporates due to stupidity.")


def shady_kitchen():
    print_pause("As you open the door you find a shady"
                "looking kitchen...yikes or..wow?")
    choice_2 = valid_input(
        "Do you inspect the kitchen hoping to find dragon glass or pass on "
        "saying its not woth the risk?", ["inspect", "pass"])
    if "inspect" in choice_2:
        print_pause("You find einstien's notebook in the rubble.Wow")
        question(
            "I have cities, but no houses. I have mountains, but no trees. "
            "I have water, but no fish. What am I?\n--->",
            "map")
    elif "pass" in choice_2:
        print_pause("Nice decision!!,the kitchen was filled"
                    " with undetectable poisonous gas!!")
        question(
            "I have cities, but no houses. I have mountains, but no trees. "
            "I have water, but no fish. What am I?\n--->",
            "map")
    else:
        print_pause("You inhale the toxic fumes unknowingly and die.SADGE")


def question(question, answer):
    print_pause("You are now bombarded with a riddle,"
                "answer as your life depends on it")
    print_pause("get the answer right and u shall attain what "
                "you seek..get it wrong and die..")
    q = input(question)
    if answer in q:
        print_pause("Congrats on the right answer!!")
        print_pause(
            "You suddenly find youself healed mentally and physically and "
            "the dragonglass slowly appears in your hand.REJOICE!")
        print_pause("You gain immense treasure and you find a spin and "
                    "win wheel that times your treasure.nicee :D")
        chosen_number = random.randint(1, 101)
        print("congrats,the wheel spins in your favour and "
              f"you gain {chosen_number} times the treasure!")
    else:
        print_pause("You get the answer wrong and meet your ugly death. :3"
                    "You sink into the darkness")
# valid_input cannot be used here as there is only one chance to get
# the correct answer,if there are 2 or more chances
# else statement gets nullified..and the game doesnt end..


start()

while True:
    replay = valid_input("would you like to play again? \n--->", ["yes", "no"])
    if "yes" in replay:
        start()
    else:
        print("thanks for playing!")
        break
