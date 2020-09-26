from first_task import mult_2_generator
from second_task import emit_lines


if __name__ == "__main__":
    print("FIRST TASK")
    print("~" * 40)
    for i in mult_2_generator(2, 20):
        print(i)
    print("~" * 40)

    print("\nSECOND TASK")
    print("~" * 40)
    for i in emit_lines('test', 'qwe'):
        print(i)
    print("~" * 40)
