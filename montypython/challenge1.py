#!/usr/bin/python3

def main():

    round = 0
    answer = " "
    while round < 3 and answer.lower() != "brian":
        round += 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        if answer.lower() == "brian": # logic to check if user gave correct answer
            print("Correct!")
        elif round == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
        else:                 # if answer was wrong
            print("Sorry. Try again!")






if __name__ == "__main__":
    main()
