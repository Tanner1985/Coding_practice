#Main Game function
def main():
    random_number = generateRandomNumber()
    guess = int(input('This is a random number guessing game! Please enter your guess: '))
    #Check if the guess is correct, keeping track of the number of guesses
    num_guesses = 0
    while(guess != random_number):
        if(guess < random_number and guess < (random_number - 10)):
            print('Too low!')
        elif(guess > random_number and guess > (random_number + 10)):
            print('Too high!')
        elif(guess > random_number and not guess > (random_number + 10)):
             print('Getting warm but still high!')
        elif(guess < random_number and not guess < (random_number - 10)):
            print('Getting warm but still Low!')
        else:
            print('Error!')
        num_guesses = num_guesses + 1
        guess = int(input('Please enter your guess: '))
    print(f'Well done! You have guessed the number in {num_guesses} guesses!')
    #Ask the user if they would like to play again
    play_again = input('Would you like to play again? (yes or no): ')
    if(play_again == 'yes'):
            main()
    else:
        print('Thank you for playing!')   
#Generate Random Number
def generateRandomNumber():
    import random
    random_number = random.randint(1,1000)
    return random_number

main()