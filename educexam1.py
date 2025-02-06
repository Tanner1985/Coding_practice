#Simple script to ask questions and print answers for study
def main():
    questionNum = random_number()
    question_list = questionList()
    answer_list = answerList()
    answer = input(f'{question_list[questionNum]}')
    print(f'You answered: {answer}')
    print(f'The correct answer is: {answer_list[questionNum]}')
    play_again = input('Would you like to play again? (yes or no): ')
    if(play_again == 'yes'):
        main()
    else:
        print('Thank you for playing!')

def random_number():
    import random
    random_number = random.randint(0,9)
    return random_number

def questionList():
    question_list = ['What is the capital of France?', 'What is the capital of Germany?', 'What is the capital of Italy?', 'What is the capital of Spain?', 'What is the capital of the United States?', 'What is the capital of Canada?', 'What is the capital of Mexico?', 'What is the capital of Brazil?', 'What is the capital of Argentina?', 'What is the capital of Australia?']
    return question_list
def answerList():
    answer_list = ['Paris', 'Berlin', 'Rome', 'Madrid', 'Washington D.C.', 'Ottawa', 'Mexico City', 'Brasilia', 'Buenos Aires', 'Canberra']
    return answer_list