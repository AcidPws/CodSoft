class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        self.score = 0 #if the player wants to play again, it is so that score gets reset to zero
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question.text}")
            for j, option in enumerate(question.options, start=1):
                print(f"{j}. {option}")

            user_answer = int(input("Enter the number as your answer: "))
            if question.is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.options[question.correct_option - 1]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


# Sample questions
questions_list = [
    Question("What is the capital of France?", ["Paris", "Berlin", "London"], 1),
    Question("Which programming language is this quiz written in?", ["Python", "Java", "C++"], 1),
    Question("What is 2 + 2?", ["3", "4", "5"], 2),
    Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus"], 2),
    Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen"], 2),
    Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe"], 2),
]

# Create a Quiz instance and start the quiz
quiz = Quiz(questions_list)
quiz.start_quiz()

#to play again
again = input("Want to play again?y/n: ")
while again=="y":
    quiz.start_quiz()
    again = input("Want to play again?y/n: ")

