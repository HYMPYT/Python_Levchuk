from task_1 import task_1_execute
from task_2 import task_2_execute
import task_3
import task_4
import task_5
import task_6

if __name__ == "__main__":
    #! CONSTS
    TASK_1 = "1"
    TASK_2 = "2"
    TASK_3 = "3"
    TASK_4 = "4"
    TASK_5 = "5"
    TASK_6 = "6"
    EXIT = "q"

    while True:
        print(f"""
        Choices:
        TASK_1 -> {TASK_1}
        TASK_2 -> {TASK_2}
        TASK_3 -> {TASK_3}
        TASK_4 -> {TASK_4}
        TASK_5 -> {TASK_5}
        TASK_6 -> {TASK_6}
        EXIT -> {EXIT}
        -------------------------
        """)
        choice = input("Your choice: ")
        
        if choice == EXIT:
            break

        elif choice == TASK_1:
            task_1_execute("./Files/file_1_1.txt", "./Files/file_1_2.txt")
            input("Press Enter to continue...")

        elif choice == TASK_2:
            task_2_execute("./Files/file_2.txt")
            print('The answer is written to a file "answer_for_task_2.txt"')
            input("Press Enter to continue...")

        elif choice == TASK_3:
            deleted_string = task_3.delete_last_line_from_file("./Files/file_3.txt")
            if deleted_string:
                task_3.write_result("./Files/answer_for_task_3.txt", deleted_string)
                print('The answer is written to a file "answer_for_task_3.txt"')
            else:
                print("File is empty.")
            input("Press Enter to continue...")

        elif choice == TASK_4:
            lenght = task_4.get_length_of_the_longest_line("./Files/file_4-5.txt")
            print(f"The lenght of the longest line in file: {lenght}")
            input("Press Enter to continue...")

        elif choice == TASK_5:
            word = input("Enter the word: ")
            res = task_5.get_number_of_a_given_word("./Files/file_4-5.txt", word)
            print(f"The word entered in the file occurs so many times: {res}")
            input("Press Enter to continue...")

        elif choice == TASK_6:
            old_word = input("Enter the word you want to replace: ")
            new_word = input("Enter the word you want to replace the old word with: ")
            task_6.replace("./Files/file_6.txt", old_word, new_word)
            print('The file "file_6.txt" has been overwritten')
            input("Press Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")