import tkinter as tk
import yaml
import random

class QuizApp:
    def __init__(self, root, quiz_data):
        self.root = root
        self.root.title("Quiz App")
        self.questions = quiz_data
        random.shuffle(self.questions)
        
        self.total_questions = len(self.questions)
        self.score = 0

        self.prompt_label = tk.Label(self.root)
        self.prompt_label.pack(pady=5)

        self.next_question()


    def next_question(self):

        # check we acutally have questions left
        if not self.questions:
            self.show_result()
            return

        # ask this question
        self.clear_options()
        self.current_question = self.questions.pop()

        # set prompt
        self.prompt_label.config(text=self.current_question["prompt"])

        # display options
        options = self.current_question["options"]
        random.shuffle(options)
        for option in options:
            button = tk.Button(self.root, text=option, command=lambda opt=option: self.check_answer(opt))
            button.pack(pady=5)

    def clear_options(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

    def check_answer(self, selected_option):
        correct_answer = self.current_question["answer"]
        # Check if the answer is correct
        if selected_option == correct_answer:
            self.score += 1
            self.next_question()
        else:
            # display the correct answer
            self.clear_options()
            self.prompt_label.config(text=f"{self.current_question['prompt']}\nCorrect answer: {correct_answer}")
            # make sure the user is ok with this
            button = tk.Button(self.root, text="Next", command=self.next_question)
            button.pack(pady=5)

    def show_result(self):
        self.clear_options()
        self.prompt_label.config(text=f"Quiz Completed\nYour score: {self.score}/{self.total_questions}") 
        button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        button.pack(pady=5)

# Load your quiz data from YAML
with open("quiz_data.yaml", "r") as file:
    quiz_data = yaml.safe_load(file)

# Create and run the Tkinter app
root = tk.Tk()
app = QuizApp(root, quiz_data)
root.mainloop()
