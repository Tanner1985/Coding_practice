#Simple script to ask questions and print answers for study
def main():
    questionNum = random_number()
    question_list = questionList()
    answer_list = answerList()
    answer = input(f'{question_list[questionNum]}: ')
    print(f'You answered: {answer}')
    print(f'The correct answer is: {answer_list[questionNum]}')
    play_again = input('Would you like to play again? (yes or no): ')
    if(play_again == 'yes'or 'Yes' or 'YES'):
        main()
    else:
        print('Thank you for playing!')

def random_number():
    import random
    random_number = random.randint(0,9)
    return random_number

def questionList():
    question_list = ['Which of Coveys Four Quadrants should you focus on? Give Two examples and explain why to focus here.', ' List your top two Learning Preferences and two study skills for each. Explain the Skills', 'What is Growth Mindset and Fixed Mindset. How do you use Growth Mindset?', 'What are three of the seven keys to college success? Explain the three you pick.', 'List three costs of procrastination and how to avoid them', 'List the four external factors of strategic learning', 'List the three internal elements of strategic learning and give 2 examples of each.', 'List the five aspects of motivation and give an example in your life that fits them all.', 'What three things make a value a “core” value. Choose one of your own and explain how they apply to it.', 'What are the 6 factors of metacognition']
    return question_list
def answerList():
    answer_list = ['Second Quadrant, examples include Exercise, personal relationships and planning. Focusing here helps with health, stress and preventing emergencies.' , 'Preferences include: Verbal-linguistic, intrapersonal, interpersonal, mathematical-logical , naturalistic, visual-spatial, body-kinesthetic.', 'Growth mindset is the belief that you can improve yourself through effort, fixed is the mindset that your skills are set in place.', ' Show up, Preparation, Time management, Effort, Motivation, Get help when you need it, learn from everything.', 'Costs of procrastination include stress, grades lowing, missing assignments, lower self esteem. Be able to elaborate. Ways to avoid them include planning and getting help when needed. Be able to elaborate here as well.', 'Teachers expectations, Task requirements, Resources, Social Support', 'Skill: Self as a learner. Note taking and using Will: Setting, analyzing and using goals. Future time perspective Self-regulation: Concentration. Coping with academic worry and anxiety.', 'Choice, Effort, Persistence, Cognitive Engagement, Achievement. Example are personal', 'Freely chosen, affirmed and prized publicly, modeled for others. Examples are personal.', ' Self Awareness, Task Awareness, Strategy Awareness, Strategy Selection, Goal Setting, Self-monitoring.' ]
    return answer_list

main()