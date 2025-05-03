import tkinter as tk
from tkinter import messagebox

"""
The game is a Questionnaire of fun facts about Ariana Grande. 
There is 5 questions with multiple choice answer.
You can not move on until you answer the current question at hand.
While answers, the screen will turn green if you select the right answer but
turns red if you do not. At the end you will recieve your score out of 5.
"""

# List with the questions and their respected multiple choice answer
questions = [
    {
        "question": "What was Ariana Grande's first album?",
        "options": ["My Everything", "Yours Truly", "Dangerous Woman", "Sweetener"],
        "answer": "Yours Truly"
    },
    {
        "question": "Which TV show did Ariana first star in?",
        "options": ["iCarly", "Hannah Montana", "Victorious", "Sam & Cat"],
        "answer": "Victorious"
    },
    {
        "question": "What is Ariana allergic to?",
        "options": ["Cats", "Dogs", "Shellfish", "Eggs"],
        "answer": "Cats"
    },
    {
        "question": "Where was Ariana Grande born?",
        "options": ["New York", "Los Angeles", "Miami", "Boca Raton"],
        "answer": "Boca Raton"
    },
    {
        "question": "What is Ariana's favorite color?",
        "options": ["Pink", "Lavender", "Blue", "Red"],
        "answer": "Lavender"
    }
]

class ArianaQuiz:
    def __init__(self, root):
        # This is for the main window info
        self.root = root
        self.root.title("Ariana Grande Quiz")
        # I just chose this because on google it says this is the avg. size of a window screen
        self.root.geometry("1920x1080")
        self.root.config(bg='pink')

        # Initialize score and question index
        self.score = 0
        self.qIndex = 0

        # Quiz title
        self.title = tk.Label(root, text="Ariana Grande Quiz", fg="black", font=("Geneva", 20, "bold"))
        self.title.pack(pady=20)

        # "How to Play" button
        self.howToPlayBtn = tk.Button(root, text="How to Play", font=("Geneva", 12), command=self.showHowToPlay)
        self.howToPlayBtn.pack(pady=10)

        # Question text
        self.qText = tk.Label(root, text="", fg="black", font=("Geneva", 14), wraplength=400)
        self.qText.pack(pady=10)

        # Answer buttons
        self.buttons = []
        for i in range(4):
            # Create each button and attach click handler
            btn = tk.Button(root, text="", font=("Geneva", 12), width=30, command=lambda i=i: self.checkAnswer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Next button to go to the next question
        self.nextBtn = tk.Button(root, text="Next", font=("Geneva", 12), command=self.nextQuestion, state=tk.DISABLED)
        self.nextBtn.pack(pady=20)

        # Show the first question
        self.showQuestion()

    def showQuestion(self):
        # Display the current question and reset background colors if need be
         
        # Reset background color to pink
        self.root.config(bg='pink')
        self.title.config(bg='pink')
        self.howToPlayBtn.config(bg='pink')
        self.qText.config(bg='pink')
        self.nextBtn.config(bg='pink')

        # Set question text
        self.qText.config(text=questions[self.qIndex]["question"])
        
        # Loop through each option and set the button text and default pink background
        options = questions[self.qIndex]["options"]
        index = 0
        for opt in options:
            self.buttons[index].config(text=opt, state=tk.NORMAL, bg='pink')
            index += 1

        # Disable Next button until an answer is selected
        self.nextBtn.config(state=tk.DISABLED)

    def checkAnswer(self, i):
        # Check if the selected answer is correct and highlight appropriately.
         
        selected = questions[self.qIndex]["options"][i]
        correct = questions[self.qIndex]["answer"]

        if selected == correct:
            # If correct, turn button green and increase score
            self.root.config(bg='green')  # Change background to green
            self.title.config(bg='green')
            self.qText.config(bg='green')
            self.score += 1
        else:
            self.root.config(bg='red')  # Change background to red
            self.title.config(bg='red')
            self.qText.config(bg='red')

        # Disable all buttons after selection
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

        # Enable Next button
        self.nextBtn.config(state=tk.NORMAL)

    def nextQuestion(self):
        # Move to the next question or end the quiz if finished.
         
        self.qIndex += 1
        if self.qIndex < len(questions):
            # Show next question
            self.showQuestion()
        else:
            # Show final score and close the quiz
            messagebox.showinfo("Final Score", f"You got {self.score}/{len(questions)} correct!")
            self.root.destroy()

    def showHowToPlay(self):
        # Show a popup window with how to play
        
        howWin = tk.Toplevel(self.root)
        howWin.title("How to Play")
        howWin.geometry("500x400")
        howWin.config(bg='pink')

        instructions = (
            "Welcome to the Ariana Grande Quiz!\n\n"
            "HOW TO PLAY:\n"
            "💍 Read each question carefully.\n"
            "💍 Click on the option you think is correct.\n"
            "💍 If you're right, the background turns green.\n"
            "💍 If you're wrong, the background turns red.\n"
            "💍 Click 'Next' to move to the next question.\n"
            "💍 At the end, your total score will be shown.\n"
            "💍 HAVE FUN!"
        )

        label = tk.Label(howWin, text=instructions, fg="black", font=("Geneva", 12), wraplength=480, justify="left", bg='pink')
        label.pack(pady=20, padx=10)

        closeBtn = tk.Button(howWin, text="Close", command=howWin.destroy, font=("Geneva", 12), bg='pink')
        closeBtn.pack(pady=10)


root = tk.Tk()
quiz = ArianaQuiz(root)
root.mainloop()
