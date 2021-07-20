from tkinter import *
from questions import *
from tkinter import messagebox


index = 0  # variable to store question index 
score = 0  # variable to store score 


def update_score(choice):
    '''Updates the score of player'''
    global score
    if choice == questions[index]["correct"]: # Increment score if chice matches the correct option
        score = score + 1


def game_over():
    ''' Removes all the radio buttons and shows score'''
    for rad_button in radio_btns.values():
        rad_button.destroy() # destroy all the radio buttons 
    question.destroy() # destroy the question  element 
    label.config(text="Game Over \n Your Score is " + str(score)) # show final score
    button.config(text = "Quit", command = root.destroy) # Close Window


def deselect_radiobtn():
    ''' Deselects all the radio buttons '''
    for button in radio_btns.values():
        button.deselect()


def next_question():
    ''' Update the text values of elements according to the index of question'''
    global index
    # update the label , questions and radio buttons 
    label.config(text = " Question "+ str(index+1) + "/" + str(len(questions))) 
    question.config(text=questions[index]["question"])
    for key, value in questions[index]["options"].items():
        radio_btns[key].config(text = value)
    choice.set('z') # reset the shared variable 


def next_set():
    ''' Validate and update '''
    global index
    if choice.get() == 'z': # if no options is chosen show popup
        messagebox.showinfo("Message", "No, Options selected")
        return
    update_score(choice.get())
    if index == len(questions) - 1:
        game_over() # if last question show game over screen
        return 
    deselect_radiobtn()
    index = index + 1 # increment index
    next_question()


root = Tk()
root.title("Quiz App")
root.geometry("350x350")

choice = StringVar(value='z')

label = Label(root, text="Quiz App\n" + " Question "+ str(index+1) + "/" + str(len(questions)), font="30")
question = Label(root, text=questions[index]["question"], font="30",pady="5px")
r1 = Radiobutton(root, text=questions[index]["options"]["a"], variable=choice, value="a", font="24")
r2 = Radiobutton(root, text=questions[index]["options"]["b"], variable=choice, value="b", font="24")
r3 = Radiobutton(root,text=questions[index]["options"]["c"], variable=choice, value="c", font="24")
r4 = Radiobutton(root, text=questions[index]["options"]["d"], variable=choice, value="d", font="24")
button = Button(root, text="Next", command = next_set, font="30", border="2")

radio_btns = {'a': r1, 'b': r2, 'c': r3, 'd': r4} # creating a dict to make changes in radio button easier 

label.pack() 
question.pack()
for btn in radio_btns.values():
    btn.pack()
button.pack()

root.mainloop()
