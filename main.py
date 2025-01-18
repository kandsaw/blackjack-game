import random
import art


def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game=input("do you want to play the game blackjacktype 'yes'or 'no' :")
    if game == 'yes':
        print(art.logo)
        your_cards=random.sample(cards,2)
        total=sum(your_cards)
        computer_cards=random.sample(cards,2)
        total2=sum(computer_cards)

        print(f"your cards :{your_cards}current score:{total},\n")
        print(f"the computer cards :{computer_cards}current score:{total2},\n")


        def play_one_more():
            while True :
                add_cort=input("type 'yes' to get another card, type 'no' to pass:")
                if add_cort == 'yes':
                    new_card=random.choice(cards)
                    your_cards.append(new_card)
                    total=sum(your_cards)
                    new_computer_card=random.choice(cards)
                    computer_cards.append(new_computer_card)
                    total2=sum(computer_cards)

                    # printing the total number of the playe
                    print(f"your cards are:{your_cards}, and teh current score is:{total}")
                    # printing the total number of the compute
                    print(f"computer's cards are:{your_cards}, and the total is:{total2}")
                    if total > 21 and 11 in your_cards:
                        your_cards[your_cards.index(11)] = 1
                        total = sum(your_cards)
                    if total2>total or total>21:
                        print("you lose")
                        play_game()
                    if total<total2 :
                        print("you win")
                    else:
                        play_one_more()

                else:
                    print(f"your cards are:{your_cards}, and teh current score is:{total}")
                    print(f"computer's cards are:{your_cards}, and the total is:{total2}")
                    if total2 > total:
                        print("you lose")
                        play_game()
                    else:
                        play_more()

        play_one_more()


    else :
        print("ok do not play")





play_game()












































