# 100 days of code python 
import os
import random 


# # 1. Band Name Generator
# print(f"Hi! This is a band name generator.")
# city_name = input("What is the name of the city you grew up in?\n")
# pet_name = input("What is the name of your first pet?\n")
# band_name = city_name + " " + pet_name
# print(f"Your band name is {band_name}!")

# # 2. Tip Calculator 
# print("Welcome to the tip calculator!")
# total_bill = float(input(f"What is the total bill? - $"))
# tip_pct = float(input(f"How much would you like to tip? (5%, 10%, 15%) - %"))
# num_persons = int(input(f"How many people to split the bill? - "))
# final_bill = total_bill * (1+(tip_pct)/100)
# print(f"Each person will pay - ${(final_bill/num_persons):.2f}")

# # 3. Treasure Hunt - skipped too big too boring 


# # 4. Rock Papers and Scissors 
# from common import STR_RPS 
# valid_moves = {
#     0: "Rock",
#     1: "Paper",
#     2: "Scissors"
# }

# while True:
#     player_move = int(input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
#     print(f"You choose {valid_moves[player_move]} - \n {STR_RPS[player_move]} \n")
#     ai_move = random.choice(list(valid_moves.keys()))
#     print(f"AI choose {valid_moves[ai_move]} - \n {STR_RPS[ai_move]} \n")

#     if player_move == ai_move:
#         print(f"This is a draw! Try again")
#     elif (player_move == 0 and ai_move == 2 )\
#      or (player_move == 1 and ai_move == 2)\
#      or (player_move == 3 and ai_move == 0):
#         print(f"PLAYER WINS! :)")
#         break
#     else:
#         print(f"AI WINS! :(") 
#         break


# # 5. Password Generator 
# print(f"Welcome to the PyPassword Generator!")
# letters = [i for i in 'abcdefghijklmnopqrstuvwxyz']
# numbers = [i for i in range(0, 10)]
# symbols = [i for i in '!@#$%^&*()']
# num_letters = int(input(f"How letters do you want in your password? - ") or 3)      # with a default value
# num_numbers = int(input(f"How numbers do you want in your password? - ") or 3)
# num_symbols = int(input(f"How symbols do you want in your password? - ") or 3)
# selected_char = []
# selected_char.extend(random.choices(letters, k=num_letters))
# selected_char.extend(random.choices(numbers, k=num_numbers))
# selected_char.extend(random.choices(symbols, k=num_symbols))
# random.shuffle(selected_char)
# new_password = ''.join([str(i) for i in selected_char]) 
# print(f"\n Here is your new password - {new_password}")

# # # 6. Robot Manipulation - Interactive Excersice 
# check at - 


# # 7. Skipped 


# # 8. Ceaser cipher 
# while True:
#     action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     message = input("Type your message:\n").lower()
#     shift = int(input(f"Type the shift number:\n"))
#     letters = [i for i in 'abcdefghijklmnopqrstuvwxyz']
#     letters_shifted = letters[shift:] + letters[:shift] 
#     if action == "encode":
#         cipher_dict = dict(zip(letters, letters_shifted))
#     else: 
#         cipher_dict = dict(zip(letters_shifted, letters))
#     result = [cipher_dict[i] if i in letters else i for i in message]
#     result = ''.join(result)
#     print(f"Here's the {action}d result: {result}")
#     _exit = input("Type 'yes' if you want to go again. Othewise type 'no'\n")
#     print("\n")
#     if _exit == "yes":
#         continue
#     break 
        
# # 9. Blind Auction Program 
# all_bids = dict()
# while True:
#     name = input("What is your name?: ")
#     bid = int(input("What is your bid?: $"))
#     all_bids[name] = bid

#     next_bidder = input(f"Are there any other bidders? Type 'yes' or 'no'\n")
#     if next_bidder == 'yes':
#         os.system('clear')
#     else:
#         break
# winner = sorted(all_bids.items(), key=lambda x:x[1], reverse=True)[0]
# os.system('clear')
# print(f"The winner is {winner[0]} with a bid {winner[1]}")

# # 10.
# operators = ['+', '-', '*', '/']
# while True: 
#     operand_1 = float(input("What is your first number?: "))
#     print(*operators, sep="\n")
#     while True:
#         operator = input(f"Pick an operation: ")
#         if operator not in operators:
#             print("Invalid selection! Try again")
#             continue 
#         operand_2 = float(input("What is your next number?: "))
#         expr = f"{operand_1} {operator} {operand_2}"
#         result = round(eval(expr), 3)
#         print(f"{expr} = {result}")
#         action = input(f"Type 'y' to continue with {result}, 'n' for a new calculation: ")
#         if action == 'y':
#             operand_1 = result
#             continue 
#         else:
#             os.system('clear')
#             break

class Foo:
    pass



class Bar:
    pass


# # 11. BlackJack
cards =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def print_stats(player_cards, ai_cards):
    print(f"\tyou cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"\tcomputer's fiwst card: {ai_cards[0]}")

def play_game():
    player_cards = []
    ai_cards = [] 
    
    player_cards.extend(random.choices(cards, k=2))
    ai_cards.append(random.choice(cards))
    print_stats(player_cards, ai_cards)
    
    while True:
        hit = input(f"Type 'y' to get another card, 'n' to pass: ")
        if hit == 'y':
            player_cards.append(random.choice(cards))
            print_stats(player_cards, ai_cards)
        else:
            break 

    if sum(player_cards) > 21:
        print("You went over! You lose.") 
        return 

    while True:
        # AI draws 
        if sum(ai_cards) > 21:
            print(f"Computer goes over! You win!")
            return 

        if sum(ai_cards) < 17:
            ai_cards.append(random.choice(cards))
        else:
            break        

    player_score = sum(player_cards)
    ai_score = sum(ai_cards)
    if player_score > ai_score:
        print("You win!")
    else:
        print("You lose!")
    return 

while True:
    run_game = input("\n\nDo you want to run the game of blackjack? 'y' or 'n': ")
    if run_game == 'y':
        play_game()
    else:
        break