# this file helps us to add and update the question in the question list
from qdata import que_data
# this class contains two static methods
class QuestionManager:
    @staticmethod
    def add_que():
        text = input('Enter question:\n')
        options = {}
        for i in ['a','b','c','d']:
            options[i] = input(f'Enter option {i}: ')
        answer = input(f"Enter the single correct option: ").lower()
        que_data.append({
            'text': text,
            'options': options,
            'answer': answer
        })
        print('New question added')


    @staticmethod
    def update_que():
        que_text = input('Enter the existing question text that you want to replace: \n').lower()
        que_update = input('Enter the updated question text that you want to update: \n')
        for q in que_data:
            if que_text in q['text'].lower():
                q['text'] = que_update
                print('Question updated\n')
                break
        else:
            print('Question not found\n')







