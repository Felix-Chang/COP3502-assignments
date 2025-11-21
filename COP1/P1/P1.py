import p1_random as p1
rng = p1.P1Random()

replay = True
game_number = 0
player_wins = 0
dealer_wins = 0
ties_count = 0

while replay:
    player_total = 0
    game_over = False
    print(f"START GAME #{game_number + 1}\n")

    # Initial Card
    init_card = rng.next_int(13) + 1

    if init_card == 1:
        player_total = 1
        print("Your card is a ACE!")
    elif (init_card > 1) and (init_card < 11):
        player_total = init_card
        print(f"Your card is a {init_card}!")
    elif init_card == 11:
        player_total = 10
        print("Your card is a JACK!")
    elif init_card == 12:
        player_total = 10
        print("Your card is a QUEEN!")
    elif init_card == 13:
        player_total = 10
        print("Your card is a KING!")

    # Display Player hand
    print(f"Your hand is: {player_total}\n")
    
    # Loop Player Actions until blackjack or bust i.e. game over
    while not game_over:
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            curr_card = rng.next_int(13) + 1
            
            # Add corresponding amount depending on card and display card
            if curr_card == 1:
                player_total += 1
                print("\nYour card is a ACE!")
            elif (curr_card > 1) and (curr_card < 11):
                player_total += curr_card
                print(f"\nYour card is a {curr_card}!")
            elif curr_card == 11:
                player_total += 10
                print("\nYour card is a JACK!")
            elif curr_card == 12:
                player_total += 10
                print("\nYour card is a QUEEN!")
            elif curr_card == 13:
                player_total += 10
                print("\nYour card is a KING!")
            
            # Show Player Hand
            print(f"Your hand is: {player_total}\n")
                
            # Check for blackjack or bust
            if player_total == 21:
                game_over = True
                player_wins += 1
                game_number += 1
                print("BLACKJACK! You win!\n")
            elif player_total > 21:
                game_over = True
                dealer_wins += 1
                game_number += 1
                print("You exceeded 21! You lose.\n")

        elif choice == "2":
            dealer_total = rng.next_int(11) + 16

            # Check Dealer for blackjack, bust or tie
            if dealer_total == player_total:
                print(f"\nDealer's hand: {dealer_total}")
                print(f"Your hand is: {player_total}\n")
                game_over = True
                ties_count += 1
                game_number += 1
                print("It's a tie! No one wins!\n")
            else:
                if dealer_total == 21:
                    print(f"\nDealer's hand: {dealer_total}")
                    print(f"Your hand is: {player_total}\n")
                    game_over = True
                    dealer_wins += 1
                    game_number += 1
                    print("Dealer wins!\n")
                elif dealer_total > 21:
                    print(f"\nDealer's hand: {dealer_total}")
                    print(f"Your hand is: {player_total}\n")
                    game_over = True
                    player_wins += 1
                    game_number +=1
                    print("You win!\n")
                else:
                    if player_total > dealer_total:
                        print(f"\nDealer's hand: {dealer_total}")
                        print(f"Your hand is: {player_total}\n")
                        game_over = True
                        player_wins += 1
                        game_number += 1
                        print("You win!\n")
                    else: 
                        print(f"\nDealer's hand: {dealer_total}")
                        print(f"Your hand is: {player_total}\n")
                        game_over = True
                        dealer_wins += 1
                        game_number += 1
                        print("Dealer wins!\n")
        elif choice == "3":
            print(f"\nNumber of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties_count}")
            print(f"Total # of games played is: {game_number}")
            print(f"Percentage of Player wins: {(player_wins / game_number * 100):.1f}%\n")
        elif choice == "4":
            game_over = True
            replay = False
        else:
            print("Invalid input!\n")
            print("Please enter an integer value between 1 and 4.")