def validation_human_answer(max_answer: int, min_answer: int) -> int:

        while True:
            human_answer_string = input(f"Какое действие выбираете: ")
            
            if not human_answer_string.isdigit() or int(human_answer_string) > max_answer or int(human_answer_string) < min_answer:
                print("Повторите ввод действия")
                continue
            try:
                human_answer_namber = int(human_answer_string)
                break
            except ValueError:
                print("Повторите ввод действия")
                continue
        return human_answer_namber