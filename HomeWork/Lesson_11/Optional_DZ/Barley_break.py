from random import randint, shuffle

# Constants
I_ZERO = 0
J_ZERO = 0
SIZE = 4

# Blanks for displaying the field
UP = """+-----+-----+-----+-----+
|     |     |     |     |"""
MID = """|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |"""
BOT = """|     |     |     |     |
+-----+-----+-----+-----+"""

# Condition of end the game
END = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def filling_filed(lst):
    """This function returns a matrix which is represented by a list with numbers in the range (0, 16)"""
    b = 1
    buf = []
    for i in range(SIZE):
        for j in range(SIZE):
            buf.append(b)
            b += 1
        lst.append(buf)
        buf = []
    lst[SIZE - 1][SIZE - 1] = 0
    return lst

def randome_filling(lst):
    """This function return the shuffled list"""
    for i in range(SIZE):
        shuffle(lst[i])
    shuffle(lst)
    return lst

def search_for_zero(lst):
    """The function for search zero in the list"""
    global I_ZERO, J_ZERO
    for i in range(SIZE):
        for j in range(SIZE):
            if lst[i][j] == 0:
                I_ZERO = i
                J_ZERO = j
                break

def screen(lst):
    """The function for display play field"""
    print(UP)
    for i in range(SIZE):
        for j in range(SIZE):
            if lst[i][j] < 10:
                if lst[i][j] == 0:
                    print('|     ', end = '')
                else:
                    print(f'|  {lst[i][j]}  ', end = '')
            else:
                num = str(lst[i][j])
                print(f'| {num[0]} {num[1]} ', end = '')
            if j == 3 and i < 3:
                print('|')
                print(MID)
    print('|')
    print(BOT) 

def end_of_the_game(lst):
    """The function for check the end of the game"""
    if lst == END:
        print("You Win!")
        return True
    else:
        return False

def get_direction(lst):
    """The function for move fields in the play field
    UP -- W, LEFT -- A, DOWN -- S, RIGHT -- D"""
    global I_ZERO, J_ZERO
    move = input()
    if move.lower() == 'w':
        if I_ZERO >= 0 and I_ZERO <= 2:
            lst[I_ZERO][J_ZERO] = lst[I_ZERO + 1][J_ZERO]
            I_ZERO += 1
            lst[I_ZERO][J_ZERO] = 0
    elif move.lower() == 'a':
        if J_ZERO >= 0 and J_ZERO <= 2:
            lst[I_ZERO][J_ZERO] = lst[I_ZERO][J_ZERO + 1]
            J_ZERO += 1
            lst[I_ZERO][J_ZERO] = 0
    elif move.lower() == 's':
        if I_ZERO >= 1 and I_ZERO <= 3:
            lst[I_ZERO][J_ZERO] = lst[I_ZERO - 1][J_ZERO]
            I_ZERO -= 1
            lst[I_ZERO][J_ZERO] = 0
    elif move.lower() == 'd':
        if J_ZERO >= 1 and J_ZERO <= 3:
            lst[I_ZERO][J_ZERO] = lst[I_ZERO][J_ZERO - 1]
            J_ZERO -= 1
            lst[I_ZERO][J_ZERO] = 0
    return lst

if __name__ == "__main__":
    lst = []
    lst = filling_filed(lst)
    lst = randome_filling(lst)
    search_for_zero(lst)
    screen(lst)
    while not end_of_the_game(lst):
        lst = get_direction(lst)
        screen(lst)