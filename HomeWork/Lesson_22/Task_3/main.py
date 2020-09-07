from money import Money


if __name__ == "__main__":
    #! CONSTS
    UAH = "uah"
    RUB = "rub"
    USD = "usd"
    EUR = "eur"
    CENT = "cent"
    KOPECK = "kop"
    DISPLAY = "dis"
    EXIT = "q"

    while True:
        print(f"""
        Choices:
            UAH = {UAH}
            RUB = {RUB}
            USD = {USD}
            EUR = {EUR}
            EXIT = {EXIT}
        ----------------------
        """)
        choice = input("Enter choice: ")

        if choice == EXIT:
            break 

        elif choice == UAH:
            uah = input("Enter the amount in UAH: ")
            money = Money(UAH=uah)

            print(money.UAH)
            input("Press Enter to continue...")

            while True:
                print(f"""
                Choices:
                    CHANGE_UAH = {UAH}
                    CHANGE_KOPECK = {KOPECK}
                    DISPLAY = {DISPLAY}
                    EXIT = {EXIT}
                ----------------------
                """)

                choice = input("Enter choice: ")

                if choice == EXIT:
                    del money
                    break

                elif choice == UAH:
                    uah = input("Enter the amount in UAH: ")
                    money.UAH = uah
                    print(money.UAH)
                    input("Press Enter to continue...")

                elif choice == KOPECK:
                    kopeck = input("Enter the kopeck of the UAH: ")
                    money.UAH_kopeck = kopeck
                    print(money.UAH)
                    input("Press Enter to continue...")

                elif choice == DISPLAY:
                    print(money.UAH)
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == RUB:
            rub = input("Enter the amount in RUB: ")
            money = Money(RUB=rub)
            
            print(money.RUB)
            input("Press Enter to continue...")

            while True:
                print(f"""
                Choices:
                    CHANGE_RUB = {RUB}
                    CHANGE_KOPECK = {KOPECK}
                    DISPLAY = {DISPLAY}
                    EXIT = {EXIT}
                ----------------------
                """)

                choice = input("Enter choice: ")

                if choice == EXIT:
                    del money
                    break

                elif choice == RUB:
                    rub = input("Enter the amount in RUB: ")
                    money.RUB = rub
                    print(money.RUB)
                    input("Press Enter to continue...")

                elif choice == KOPECK:
                    kopeck = input("Enter the kopeck of the RUB: ")
                    money.RUB_kopeck = kopeck
                    print(money.RUB)
                    input("Press Enter to continue...")

                elif choice == DISPLAY:
                    print(money.RUB)
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")


        elif choice == USD:
            usd = input("Enter the amount in USD: ")
            money = Money(USD=usd)
            
            print(money.USD)
            input("Press Enter to continue...")

            while True:
                print(f"""
                Choices:
                    CHANGE_USD = {USD}
                    CHANGE_USD_CENT = {CENT}
                    DISPLAY = {DISPLAY}
                    EXIT = {EXIT}
                ----------------------
                """)

                choice = input("Enter choice: ")

                if choice == EXIT:
                    del money
                    break

                elif choice == USD:
                    usd = input("Enter the amount in USD: ")
                    money.USD = usd
                    print(money.USD)
                    input("Press Enter to continue...")

                elif choice == CENT:
                    cent = input("Enter the cent of the USD: ")
                    money.USD_cent = cent
                    print(money.USD)
                    input("Press Enter to continue...")

                elif choice == DISPLAY:
                    print(money.USD)
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == EUR:
            eur = input("Enter the amount in EUR: ")
            money = Money(EUR=eur)
            
            print(money.EUR)
            input("Press Enter to continue...")

            while True:
                print(f"""
                Choices:
                    CHANGE_EUR = {EUR}
                    CHANGE_EUR_CENT = {CENT}
                    DISPLAY = {DISPLAY}
                    EXIT = {EXIT}
                ----------------------
                """)

                choice = input("Enter choice: ")

                if choice == EXIT:
                    del money
                    break

                elif choice == EUR:
                    eur = input("Enter the amount in EUR: ")
                    money.EUR = eur
                    print(money.EUR)
                    input("Press Enter to continue...")

                elif choice == CENT:
                    cent = input("Enter the cent of the EUR: ")
                    money.EUR_cent = cent
                    print(money.EUR)
                    input("Press Enter to continue...")

                elif choice == DISPLAY:
                    print(money.EUR)
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")