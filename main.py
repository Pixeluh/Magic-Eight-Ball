def main():
    ### main code ###
    import intro
    import random_answers
    import user_question
    import print_answer

    intro.print_intro()
    #random_answers.random_answer()
    #user_question.ask_question()
    print_answer.print_answer(user_question.ask_question(), random_answers.random_answer())

main()
