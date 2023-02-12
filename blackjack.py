import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
wantsToPlay = False

def score(list):
    score=0
    for number in list:
        score+=number
    return score



if input(f"Do you want to play blackjack? 'y' for yes and 'n' for no: ")=="y":
    wantsToPlay = True

while wantsToPlay:
    print(logo)
    actualUserCards = [random.choice(cards), random.choice(cards)]
    actualComputerCards = [random.choice(cards), random.choice(cards)]
    wantsAnotherCard = True
    while wantsAnotherCard:
        currentUserScore = score(actualUserCards)
        currentComputerScore = score(actualComputerCards)
        print(f"Your cards: {actualUserCards}, current score: {currentUserScore}")
        print(f"First computer card: {actualComputerCards[0]}")
        if currentUserScore>21 or currentComputerScore>21 or input("Type 'y' to get another card, type 'n' to pass: ") != "y":
            wantsAnotherCard = False
        else:
            actualUserCards.append(random.choice(cards))
            actualComputerCards.append(random.choice(cards))
    
    print(f"Your cards: {actualUserCards}, final score: {currentUserScore}")
    print(f"Computer's cards: {actualComputerCards}, final score: {currentComputerScore}")

    if currentUserScore>21:
        print("You went over. You lose 😭")
    elif currentComputerScore>21:
        print("Computer went over. You WIN! 😎")
    else:
        if currentUserScore>currentComputerScore:
            print("Your score is higher than the computer. You WIN! 😎")
        elif currentComputerScore>currentUserScore:
            print("The computer's score is higher than yours.  You lose 😭")
        else:
            print("ITS A DRAW")

    if input(f"Do you want to play blackjack? 'y' for yes and 'n' for no: ")!="y":
        wantsToPlay = False


