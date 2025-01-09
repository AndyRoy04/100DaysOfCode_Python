from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 15, 'italic')

class QuizInterface:
    
    def __init__(self, quiz_questions: QuizBrain):
        self.quiz = quiz_questions
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(width=600, height=500, bg=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = Label(text='Score: 0', fg='white')
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='Question Here!', width=200, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file='100DaysOfCode_Python/Day_34/quizzler_app/images/true.png')
        false_image = PhotoImage(file='100DaysOfCode_Python/Day_34/quizzler_app/images/false.png')
        
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)
        
        self.next_question()
        
        self.window.mainloop()
        
    def next_question(self):
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.canvas.config(bg='white')
        still_has_questions = self.quiz.still_has_questions()
        if still_has_questions:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
        
    def true_button(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def false_button(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')        
        self.canvas.itemconfig(self.question_text, fill='white')
        self.window.after(1000, self.next_question)
        
