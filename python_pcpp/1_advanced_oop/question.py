import random 

class Question:
    def __init__(self, question_text, choices, correct_choice) -> None:
        self.question_text = question_text
        self.choices = choices
        self.correct_choice = correct_choice
        self.selected_answer = None

    def __str__(self) -> str:
        self_str = self.question_text + '\n\n' 
        for idx, item in enumerate(random.sample(self.choices, len(self.choices))):
            self_str += f"{idx + 1}. {item}\n"
        self.self_str = self_str
        return self.self_str
    
    def select(self, choice):
        self.selected_answer = choice

    def grade(self):
        return str(self.correct_choice) == str(self.selected_answer)

class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_choice):
        super().__init__(question_text, [True, False], correct_choice)

        if not 'True' in question_text and not 'False' in question_text:
            self.question_text = f'True/False: {self.question_text}'


class MultipleSelectQuestion(Question):
    def __init__(self, question_text, choices, correct_choice) -> None:
        super().__init__(question_text, choices, correct_choice)
        self.question_text = question_text + '(select 2)' 

    def grade(self):
        for choice in self.selected_answer:
            if str(choice) not in self.correct_choice:
                return False
        return True 
