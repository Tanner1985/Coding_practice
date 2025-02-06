#Simple script to ask questions and print answers for study
def main():
    questionNum = random_number()
    question_list = questionList()
    answer_list = answerList()
    answer = input(f'{question_list[questionNum]}: ')
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
    question_list = ['What are the four external factors in the model of strategic learning?', 'What are the three internal factors of strategic learning?', 'Give two examples of each internal factor of the stratigic learning model', 'List your top two intelligences from the multiple intelligence list', 'What are two study skills for each of your intelligences?', 'What does SMART mean when making goals?', 'What is the capital of Mexico?', 'What is the capital of Brazil?', 'What is the capital of Argentina?', 'What is the capital of Australia?']
    return question_list
def answerList():
    answer_list = ['Teachers Expectations, Current activity requirements, Social context and support, Available resources', 'Skill, Will, Self-Regulation', 'Examples can be found in Revised model PDF ', 'List found in Multiple Intelligence PDF', 'List found in Multiple Intelligence PDF.', 'Specific, Measurable, Attainable, Realistic, Timeable', 'Mexico City', 'Brasilia', 'Buenos Aires', 'Canberra']
    return answer_list

main()