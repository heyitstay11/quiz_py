import time # importing time module
from questions import * # importing questions from questions file

score = 0

def display_options(options):
    ''' displays the options '''
    for option, value in options.items():
        print(option + ' : ' + value)


def display_results():
    ''' displays result '''
    print('-----    GAME  OVER  -----\n')
    print('Your Score: ' + str(score) + '/' + str(len(questions)))


def start_game():
    ''' starts the game '''
    global score   # Uses score variable present in global scope
    for group in questions:
        print(group['question'])  #displays question
        display_options(group['options']) #display options
        user_input = input("Enter correct option (a, b, c, d) ") #takes input
        if user_input == group['correct']: #checks if answer is correct inc score by 1
            print("You are right !!")
            score += 1
        else:
            print("No, you are wrong. Correct option is " + group['correct'])
        print("Current Score: " + str(score) + "\n") #displays score
        time.sleep(1.6)  # creates a delay

    display_results()


print('''
    QUIZ TIME !!
    
    Instructions:
    1. You have 8 questions
    2. Each question has 4 options and only one is correct
    3. Correct Answer increases your score by one
    4. No negatives for wrong answers

''')

start_input = input('Press (y) to start game : ').lower()

if start_input == 'y':
    start_game()
else:
    display_results()
