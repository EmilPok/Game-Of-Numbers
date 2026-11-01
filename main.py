import random
import time
from termcolor import colored

# Endless mode
endless = 0

# Time
time_start = None
end_time = 0
speedrun_time = 0
speedrun = 0

# Players Inventory
Inventory = [
    [3] * 9,  # [0] All numbers
    {"+": 3, "-": 3, "*": 1, "/": 1}  # [1] All symbols, String:Variable eg. - Inventory[1]["+"]
]

# Score
first = True
score = 0
won_score = 100000

# Boss_Number
Boss_count = 0
Boss_num_min = 333
Boss_num_max = 999

# Target_Number and your_number
Target_die = False
Enemies_killed = 0
min_num = 1
max_num = 99
your_number = random.randint(min_num, max_num)
Target_Number = random.randint(min_num, max_num)
Enemy_die_print = []

while ((Target_Number - your_number) % 10 == 0) or ((Target_Number - your_number) == 0):  # Checks if Target Number and your_number are equal when you add them or subtract them by 10
    Target_Number = random.randint(min_num, max_num)
    test_number = (Target_Number - your_number) / 10
    if test_number == int(test_number):
        test_number = int(test_number)
Target_Number_save = Target_Number

# Attack
Number = 0
Symbol = ""
Symbol_while = True

number_position = [
    {"First": True, "First_num": 0},  # First Number, value
    {"Second": False, "Second_num": 0},  # Second Number, value
    {"Third": False, "Third_num": 0}  # Third Number, value
]

surrender = False

# Shop
bought = ""
player_choice = ""

shop_slot = [None]

inventory_slot = [None]

prices = [None]

can_buys = [None]

slots = [None]


# Functions:
def shop_slots(slot, inventory, price):
    if slot < 10:
        return slot, slot - 1, price
    else:
        slot -= 10
        if slot == 0:
            return "+", "+", 500
        elif slot == 1:
            return "-", "-", 500
        elif slot == 2:
            return "*", "*", 500
        else:
            return "/", "/", 500

def Information_print(Separation, Inventory_print_=False, string=False, reason=False):
    if speedrun:
        global end_time, speedrun_time
        end_time = time.time()
        speedrun_time = (int((end_time - time_start) * 1000)) / 1000


        # Replace all "[speedrun_time]" to a variable speedrun_time
        if string:
            string = string.replace("[speedrun_time]", f"{speedrun_time}")
        if reason:
            reason = reason.replace("[speedrun_time]", f"{speedrun_time}")

    if Separation == 1:
        print("\n------------------------------------------------------------------")
    elif Separation == 2:
        print("------------------------------------------------------------------")
    elif Separation == 3:
        print("------------------------------------------------------------------\n")
    elif Separation == 4:
        print("\n------------------------------------------------------------------\n")

    if Inventory_print_ == "num":
        print("\nYour Inventory of numbers:") 
        print(f"[ 1 - {Inventory[0][0]} ]   [ 2 - {Inventory[0][1]} ]   [ 3 - {Inventory[0][2]} ]".center(54))
        print(f"[ 4 - {Inventory[0][3]} ]   [ 5 - {Inventory[0][4]} ]   [ 6 - {Inventory[0][5]} ]".center(54))
        print(f"[ 7 - {Inventory[0][6]} ]   [ 8 - {Inventory[0][7]} ]   [ 9 - {Inventory[0][8]} ]".center(54))

    elif Inventory_print_ == "symb":
        print("\nYour symbols Inventory:")
        print(f"[ + - {Inventory[1]['+']} ]   [ - - {Inventory[1]['-']} ]   [ * - {Inventory[1]['*']} ]   [ / - {Inventory[1]['/']} ]".center(57))

    elif Inventory_print_ == "num symb":
        print("\nYour full Inventory:")
        print(f"[ 1 - {Inventory[0][0]} ]   [ 2 - {Inventory[0][1]} ]   [ 3 - {Inventory[0][2]} ]".center(54))
        print(f"[ 4 - {Inventory[0][3]} ]   [ 5 - {Inventory[0][4]} ]   [ 6 - {Inventory[0][5]} ]".center(54))
        print(f"[ 7 - {Inventory[0][6]} ]   [ 8 - {Inventory[0][7]} ]   [ 9 - {Inventory[0][8]} ]".center(54))
        print(f"[ + - {Inventory[1]['+']} ]   [ - - {Inventory[1]['-']} ]   [ * - {Inventory[1]['*']} ]   [ / - {Inventory[1]['/']} ]".center(57))


    if string:
        print(string)

    if reason:
        print(reason)


def Endless():
    global endless

    while True:
        endless = input("Would you like to enable endless mode? (Y/N) ")
        if endless.lower() == "y" or endless.lower() == "yes" or endless.lower() == "t" or endless.lower() == "true":
            endless = True
            break

        elif endless.lower() == "n" or endless.lower() == "no" or endless.lower() == "f" or endless.lower() == "false":
            endless = False
            break

        else:
            endless = False
            Information_print(1, False, "\nPlease enter either Y or N.\n")
    
    print("\n------------------------------------------------------------------\n")
    

def Speedrun():
    global speedrun
    global time_start

    while True:
        speedrun = input("Would you like to enable speedrun mode? (Y/N) ")
        if speedrun.lower() == "y" or speedrun.lower() == "yes" or speedrun.lower() == "t" or speedrun.lower() == "true":
            time_start = time.time()
            speedrun = True
            break

        elif speedrun.lower() == "n" or speedrun.lower() == "no" or speedrun.lower() == "f" or speedrun.lower() == "false":
            speedrun = False
            break

        else:
            speedrun = False
            Information_print(1, False, "\nPlease enter either Y or N.\n")


def Symbol_Check():
    global Symbol_while

    try:
        if Inventory[1][Symbol] == 0:
            if speedrun:
                Information_print(1, "symb",
                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your time: [speedrun_time]\n",
                                  f"You have zero {Symbol} in your inventory.\n")
            else:
                Information_print(1, "symb", f"Your number: {your_number}    Your target number: {Target_Number}\n",
                                  f"You have zero {Symbol} in your inventory.\n")

        else:
            Symbol_while = False

    except KeyError:
        if speedrun:
            Information_print(1, "symb",
                              f"Your number: {your_number}    Your target number: {Target_Number}    Your time: [speedrun_time]\n",
                              "You don't have this symbol in your inventory.\n")
        else:
            Information_print(1, "symb", f"Your number: {your_number}    Your target number: {Target_Number}\n",
                              "You don't have this symbol in your inventory.\n")


def surrendered(Input_Check, Separation, reason="\nYou gave up."):
    if Input_Check.lower() != "exit" and Input_Check.lower() != "quit" and Input_Check.lower() != "i give up" and Input_Check.lower() != "i surrender":
        return False

    global surrender

    if Separation:
        Information_print(Separation)
    print(reason)

    if speedrun:
        global end_time, speedrun_time
        end_time = time.time()
        speedrun_time = (int((end_time - time_start) * 1000)) / 1000
        print(f"Score: {score}    You beat {Enemies_killed} numbers    Your time: {speedrun_time}")
    else:
        print(f"Your score: {score}    You beat {Enemies_killed} numbers")

    surrender = True

    return True


def can_buy(shop_slot_0, slot_0, price_0, inventory_slot_0, can_buy_0):
    global score
    global Inventory
    global bought

    if player_choice == str(shop_slot_0) and score >= price_0:
        bought = colored(f"You bought {shop_slot_0}\n", "green")
        score -= price_0
        if str(shop_slot_0).isnumeric():
            Inventory[0][inventory_slot_0] += 1
        else:
            Inventory[1][inventory_slot_0] += 1
        return "Sold", "Sold", price_0, inventory_slot_0, False
    elif player_choice == str(shop_slot_0):
        bought = "You don't have enough score.\n"
    return shop_slot_0, slot_0, price_0, inventory_slot_0, True


def Boss_check():
    global Boss_count
    global bought
    if Boss_count < 5:
        Boss_count += 1
    else:
        bought = colored("YOU'RE FIGHTING A BOSS (higher target number)\n", "red")
        Boss_count = 0


def Shop():
    global player_choice
    global shop_slot, inventory_slot, prices, slots, can_buys
    global score
    global first
    global bought
    global Enemy_die_print

    first = True

    player_choice = 1

    shop_slot = [
        random.randint(1, 13),
        random.randint(1, 13),
        random.randint(1, 13)
    ]
    inventory_slot = [
        shop_slot[0],
        shop_slot[1],
        shop_slot[2]
    ]
    prices = [200] * 3

    # Update shops slots to correct prices and inventory_slots
    shop_slot[0], inventory_slot[0], prices[0] = shop_slots(shop_slot[0], inventory_slot[0], prices[0])
    shop_slot[1], inventory_slot[1], prices[1] = shop_slots(shop_slot[1], inventory_slot[1], prices[1])
    shop_slot[2], inventory_slot[2], prices[2] = shop_slots(shop_slot[2], inventory_slot[2], prices[2])

    slots = [
        f"{shop_slot[0]} - {prices[0]} score",
        f"{shop_slot[1]} - {prices[1]} score",
        f"{shop_slot[2]} - {prices[2]} score"
    ]

    while player_choice != "0":
        can_buys = [True] * 3

        Information_print(1, "num symb",
                          "Shop: ",
                          f"      [ {slots[0]} ]   [ {slots[1]} ]   [ {slots[2]} ]\n")
        if first:
            # Prints all things in list Enemy_die_print and remove everything in the list
            for rewards in Enemy_die_print:
                print(rewards)
            Enemy_die_print.clear()
            print("")
            first = False
        elif bought:
            print(bought)

        if speedrun:
            Information_print(False, False,
                              f"Your score: {score}    Your time: [speedrun_time]")
        else:
            print("Your score:", score)
        player_choice = input("\nWhat item would u like to buy? (0 - Close shop) ")

        if surrendered(player_choice, 4, "You gave up."):
            first = True
            return

        if player_choice == "0":
            Boss_check()
            if not bought.startswith("YOU'RE FIGHTING A BOSS"):
                bought = ""


        elif (player_choice != str(shop_slot[0]) and player_choice != str(shop_slot[1]) and player_choice != str(shop_slot[2])) or player_choice == "Sold":
            bought = "This item is not available in the store.\n"

        else:
            shop_slot[0], slots[0], prices[0], inventory_slot[0], can_buys[0] = can_buy(shop_slot[0], slots[0], prices[0], inventory_slot[0], can_buys[0])
            if can_buys[0]:
                shop_slot[1], slots[1], prices[1], inventory_slot[1], can_buys[1] = can_buy(shop_slot[1], slots[1], prices[1], inventory_slot[1], can_buys[1])
                if can_buys[1]:
                    shop_slot[2], slots[2], prices[2], inventory_slot[2], can_buys[2] = can_buy(shop_slot[2], slots[2], prices[2], inventory_slot[2], can_buys[2])

            if shop_slot[0] == "Sold" and shop_slot[0] == shop_slot[1] == shop_slot[2]:
                Boss_check()

                return


def _Target_die_():
    global Enemies_killed
    global Target_Number_save, Target_Number
    global first
    global Inventory
    global your_number
    global Target_die
    global Enemy_die_print
    global score

    # Adds score
    score += Target_Number_save * 10

    Enemies_killed += 1

    first = True

    # Adds numbers and symbols to inventory
    Target_Number_save = str(Target_Number_save)
    for number in str(Target_Number_save):
        number = int(number)
        if number == 0:
            number = random.randint(1, 9)
        Inventory[0][number - 1] += 1
        if first:
            Enemy_die_print.append("You got:")
            first = False
        Enemy_die_print.append(f"• {number}")

    for i in range(2):
        random_symbol = random.randint(0, 1)
        if random_symbol == 0: random_symbol = "+"
        if random_symbol == 1: random_symbol = "-"
        Inventory[1][random_symbol] += 1
        Enemy_die_print.append(f"• {random_symbol}")

    # Randomize new your_number and Target_Number
    your_number = random.randint(min_num, max_num)

    if Boss_count < 5:
        Target_Number = random.randint(min_num, max_num)
    else:
        Target_Number = random.randint(Boss_num_min, Boss_num_max)

    while ((Target_Number - your_number) % 10 == 0) or ((Target_Number - your_number) == 0):  # Checks if Target Number and your_number are equal when you add them or subtract them by 10
        if Boss_count < 5:
            Target_Number = random.randint(min_num, max_num)
        else:
            Target_Number = random.randint(Boss_num_min, Boss_num_max)

    Target_Number_save = Target_Number

    Target_die = False




def Attack():
    global your_number
    global Target_die
    global Target_Number
    global surrender
    global Symbol, Symbol_while
    global score
    global bought

    # Symbol check
    if all(symb == 0 for symb in Inventory[1].values()):
        if speedrun:
            Information_print(4, False,
                              "U dont have any symbols in your inventory.",
                              f"Score: {score}    You beat {Enemies_killed} numbers    Your time: [speedrun_time]")
        else:
            Information_print(4, False,
                              "U dont have any symbols in your inventory.",
                              f"Score: {score}    You beat {Enemies_killed} numbers")
        surrender = True
        return

    # Number check
    if all(num == 0 for num in Inventory[0]):
        if speedrun:
            Information_print(4, False,
                              "U dont have any numbers in your inventory.",
                              f"Score: {score}    You beat {Enemies_killed} numbers    Your time: [speedrun_time]")
        else:
            Information_print(4, False,
                              "U dont have any numbers in your inventory.",
                              f"Score: {score}    You beat {Enemies_killed} numbers")
        surrender = True
        return

    # Symbol
    if speedrun:
        Information_print(1, "symb",
                          f"Your number: {your_number}    Your target number: {Target_Number}    Your time: [speedrun_time]\n", bought)
        bought = ""
    else:
        Information_print(1, "symb",
                          f"Your number: {your_number}    Your target number: {Target_Number}\n", bought)
        bought = ""

    Symbol_while = True

    while Symbol_while:

        Symbol = input("What symbol would you like to use? ")

        if surrendered(Symbol, 1):
            return

        Symbol_Check()

    # Number
    if speedrun:
        Information_print(1, "num",
                          f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n")
    else:
        Information_print(1, "num",
                          f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n")

    Player_Number = 0
    good_number = True

    while Player_Number == 0 or not good_number:

        while True:

            Player_Number = input("What number would you like to use? (If you want to change your symbol type 'back') ")

            if surrendered(Player_Number, 1):
                return

            elif Player_Number.isdigit():

                if "0" in str(Player_Number):
                    if speedrun:
                        Information_print(1, "num",
                                          f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                          "You don't have zero in your inventory.\n")
                    else:
                        Information_print(1, "num",
                                          f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                          "You don't have zero in your inventory.\n")
                else:
                    Player_Number = int(Player_Number)
                    break
            elif Player_Number.lower() != "back":
                if speedrun:
                    Information_print(1, "num",
                                      f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                      "You didn't choose a number.\n")
                else:
                    Information_print(1, "num",
                                      f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                      "You didn't choose a number.\n")
            else:
                return

        good_number = True

        # When the player chose too high number
        if Player_Number > 999:
            if speedrun:
                Information_print(1, "num",
                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                  "You chose too high number.\n")
            else:
                Information_print(1, "num",
                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                  "You chose too high number.\n")
            good_number = False

        else:
            # For every number player typed
            for digit in str(Player_Number):

                digit = int(digit)

                # When the player doesn't have this number amount in their inventory
                if Inventory[0][digit - 1] == 0:
                    if speedrun:
                        Information_print(1, "num",
                                          f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                          f"You don't have enough {digit} in your inventory.\n")
                    else:
                        Information_print(1, "num",
                                          f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                          f"You don't have enough {digit} in your inventory.\n")
                    good_number = False
                    break


                elif number_position[2]["Third"]:
                    # Third number
                    number_position[2]["Third_num"] = digit

                    # If third and second numbers are equal
                    if number_position[2]["Third_num"] == number_position[1]["Second_num"] or number_position[2]["Third_num"] == number_position[0]["First_num"]:

                        # If first second and third numbers are equal and If player doesn't have enough numbers that are equal
                        if (number_position[2]["Third_num"] == number_position[1]["Second_num"] == number_position[0]["First_num"]) and Inventory[0][number_position[2]["Third_num"] - 1] < 3:
                            if speedrun:
                                Information_print(1, "num",
                                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                                  f"You don't have enough {digit} 's in your inventory.\n")
                            else:
                                Information_print(1, "num",
                                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                                  f"You don't have enough {digit} 's in your inventory.\n")
                            good_number = False
                            number_position[2]["Third"] = False
                            number_position[1]["Second"] = False
                            number_position[0]["First"] = True
                            break

                        # If player doesn't have enough numbers that are equal
                        elif Inventory[0][number_position[2]["Third_num"] - 1] < 2:
                            if speedrun:
                                Information_print(1, "num",
                                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                                  f"You don't have enough {digit} 's in your inventory.\n")
                            else:
                                Information_print(1, "num",
                                                  f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                                  f"You don't have enough {digit} 's in your inventory.\n")

                            good_number = False
                            break

                # Second number
                elif number_position[1]["Second"]:

                    # If second and first number are equal and If player doesn't have enough numbers that are equal
                    if (number_position[1]["Second_num"] == number_position[0]["First_num"]) and (Inventory[0][number_position[0]["First_num"] - 1] == 1):
                        if speedrun:
                            Information_print(1, "num",
                                              f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}    Your time: [speedrun_time]\n",
                                              f"You don't have enough {digit} 's in your inventory.\n")
                        else:
                            Information_print(1, "num",
                                              f"Your number: {your_number}    Your target number: {Target_Number}    Your symbol: {Symbol}\n",
                                              f"You don't have enough {digit} 's in your inventory.\n")
                        good_number = False
                        break

                    else:
                        number_position[0]["First_num"] = digit
                        number_position[1]["Second"] = True
                        number_position[2]["Third"] = True

                # First Number
                elif number_position[0]["First"]:
                    number_position[0]["First_num"] = digit
                    number_position[1]["Second"] = True


    # Subtracts a number from the player's inventory  
    # Symbol if * or / adds 50 score
    Inventory[1][Symbol] -= 1
    if Symbol == "/" or Symbol == "*":
        score += 50

    # Resets all bools
    number_position[0]["First"] = False
    number_position[1]["Second"] = False
    number_position[2]["Third"] = False

    # Checks if variables are number to subtract
    if number_position[0]["First_num"] != 0:
        number_position[0]["First"] = True
    if number_position[1]["Second_num"] != 0:
        number_position[1]["Second"] = True
    if number_position[2]["Third_num"] != 0:
        number_position[2]["Third"] = True

    # Subtracts numbers from Inventory
    if number_position[0]["First"]:
        Inventory[0][number_position[0]["First_num"] - 1] -= 1
    if number_position[1]["Second"]:
        Inventory[0][number_position[1]["Second_num"] - 1] -= 1
    if number_position[2]["Third"]:
        Inventory[0][number_position[2]["Third_num"] - 1] -= 1

    # Again resets all variables
    number_position[0]["First"] = True
    number_position[1]["Second"] = False
    number_position[2]["Third"] = False

    # Counts your_number
    your_number = eval(f"{your_number} {Symbol} {Player_Number}")
    if your_number == int(your_number):
        your_number = int(your_number)

    # Rounds a number if user uses "/"
    if Symbol == "/":
        your_number = int(your_number)

    # Checks if your_number is Target_Number
    if your_number == Target_Number:
        Target_die = True


# Main Game
Endless()
Speedrun()

# Main loop
while True:

    # When enemy die
    if Target_die:
        if score >= won_score and not endless:
            break

        _Target_die_()


        if score >= won_score and not endless:
            break

        Shop()

    if surrender:
        break

    Attack()

if score >= won_score:
    if speedrun:
        Information_print(3, False, "YOU WON !!! ",
                          f"Score: {score}    You beat {Enemies_killed} numbers    Your time: [speedrun_time] \n")

    else:
        Information_print(3, False, "YOU WON !!! ", f"Your score: {score}    You beat {Enemies_killed} numbers")
