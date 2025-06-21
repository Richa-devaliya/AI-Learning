from que_model import Question
from qdata import que_data
from question_manager import QuestionManager
from quiz import Quiz

def question_bank():
    que_bank = []
    for q in que_data:
        text = q['text']
        options = q['options']
        answer = q['answer']
        new_que = Question(text, options, answer)
        que_bank.append(new_que)
    return que_bank


def menu():
    while True:
        print("----QUIZ----")
        print('1. Add question')
        print('2. Update question')
        print('3. Show all questions')
        print('4. Take quiz')
        print('5. Exit')
        choice = input('Choose between options 1-5 :')

        if choice == '1':
            QuestionManager.add_que()
        elif choice == '2':
            QuestionManager.update_que()
        elif choice == '3':
            for q in que_data:
                print(q)
        elif choice == '4':
            que_bank = question_bank()
            quiz_test = Quiz(que_bank)
            while quiz_test.still_question():
                quiz_test.next_question()
            print(f"\nFinal Score: {quiz_test.score}/{quiz_test.question_number}")
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()



