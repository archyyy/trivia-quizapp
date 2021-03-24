import quiz_brain as qb
from ui import Ui


def click_true():
    ui.answer = "True"
    quiz_brain.check_and_score(ui.answer)
    game()
    return ui.answer


def click_false():
    ui.answer = "False"
    quiz_brain.check_and_score(ui.answer)
    game()
    return ui.answer


def click_pass():
    pass


def game():
    global i
    if i < len(quiz_brain.questions_list):
        quiz_brain.next_question(i)
        ui.change_text(quiz_brain.current_question, f"Score: {quiz_brain.score}")
        print(quiz_brain.current_answer)
        i += 1
    else:
        ui.change_text(f"FINAL SCORE: {quiz_brain.score}", "")
        ui.answer_true.config(command=click_pass)
        ui.answer_false.config(command=click_pass)


quiz_brain = qb.Brain()
quiz_brain.generate()

ui = Ui()
ui.answer_true.config(command=click_true)
ui.answer_false.config(command=click_false)

i = 0
game()
ui.window.mainloop()

