from random import randint

def game_bull(lst, number, i = -1):
    """This function returns the number of digits you guessed"""
    if len(number) > 1 and number[i] in lst:
        number.pop()
        return 1 + game_bull(lst, number)
    elif len(number) == 1 and number[i] in lst:
        return 1
    elif len(number) > 1 and not number[i] in lst:
        number.pop()
        return game_bull(lst, number)
    else:
        return 0

def game_cow(lst, number, j = -1, i = -1):
    """This function returns the number of digits you guessed and which are in their place"""
    if len(number) > 1 and number[i] == lst[j]:
        number.pop()
        return 1 + game_cow(lst, number, j - 1)
    elif len(number) == 1 and number[i] == lst[j]:
        return 1
    elif len(number) > 1 and number[i] != lst[j]:
        number.pop()
        return game_cow(lst, number, j - 1)
    else:
        return 0
    
def number_lst(number):
    """this function return the list created by number witch ordered PC or player"""
    lst = []
    while number:
        lst.append(number % 10)
        number //= 10
    lst.reverse()
    return lst

if __name__ == "__main__":
    number = randint(1000, 9999)
    lst = number_lst(number)
    count = 0
    print("~~~~~~~~~~ GAME ~~~~~~~~~~")
    print("~~~~~ Bulls and Cows ~~~~~")
    print("The computer ordered a four-digit number. Your task is to guess.")
    print("=> If you want to exit enter 0")
    while True:
        count += 1
        num = int(input("\nEnter your four-digit number -> "))
        if num >= 1000 and num < 10000:
            if num == 0:
                print("Computer's number:", number)
                break
            if  num == number:
                print("You Win!")
                print("Guesses:", count)
                break
            print("Bulls:", game_bull(lst, number_lst(num))) 
            print("Cows:", game_cow(lst, number_lst(num)))
        else:
            print("Your number must be in range(1000, 10000)")