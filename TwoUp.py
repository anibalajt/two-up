import random
lost = 0
won = 0


def get_input():
    print('\nSelect your bet.')
    print("1. HH")
    print("2. HT")
    print("3. TT")
    return int(input("Enter choice(1/2/3): "))


def coin_flip(bet):
    num = random.randint(1, 3)
    if(1 == bet and num == bet):
        ++won
        print("You won!")
    elif (2 == bet and num == bet):
        ++won
        print("You won!")
    elif (3 == bet and num == bet):
        ++won
        print("You won!")
    else:
        ++lost
        print("You lose \n")

    play = input(print("play again y/n"))
    if(play == "y"):
        main()


def main():
    user_input = get_input()
    coin_flip(user_input)


main()
