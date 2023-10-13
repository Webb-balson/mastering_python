

def guess_the_game():
    print("""
        Please Pick a number between 1 and 100, I will guess that number
        SOUNDS COOL !!! --> Let's get started
        You will only enter one of the following keys:-
        u : if my guess is higher than your number
        d : if my guess is lower than your number
        c : if my guess is CORRECT
        q : to quit

        """)
    
    numbers = range(1,101)

    while True:
        guess_number = numbers[len(numbers)//2]
        print(f"My guess is {guess_number}, is this correct ?")
        option = input("Please enter any option:- ")
        index_number = numbers.index(guess_number)

        if option == "u":
            numbers = numbers[:index_number]
            
        elif option == "d":
            numbers = numbers[index_number:]

        elif option == "c":
            print("YAY!, I won")
            break
        elif option == "q":
            print("Ok Bye !!!")
            break
        else:
            print("Please select any key from the above option only.")

    print("Run the program to play again !!!")

if __name__ == "__main__":
    guess_the_game()