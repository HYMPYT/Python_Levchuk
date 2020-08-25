from pprint import pprint
import MusicBands
import Countries


def print_result(*args) -> None:
    """Prints the elements that are passed as a parameter."""
    for element in args:
        pprint(element, width=1)
        input('Press Enter to continue...')

if __name__ == "__main__":
    # ! CONSTS
    TASK_1 = 'country'
    TASK_2 = 'music'
    MUSIC_BANDS_LIST = 'list'
    ADD_MUSIC_BAND = 'add'
    DEL_MUSIC_BAND = 'delete'
    UPDATE_MUSIC_BAND = 'update'
    SEARCH_MUSIC_BAND = 'search'
    SAVE_DATA = 'save'
    LOAD_DATA = 'load'
    COUNTRIES_LIST = 'list'
    ADD_COUNTRY = 'add'
    DEL_COUNTRY = 'delete'
    UPDATE_COUNTRY = 'update'
    SEARCH_COUNTRY = 'search'
    EXIT = 'q'
    COUNTRIES = Countries.Country()
    MUSIC_BANDS = MusicBands.MusicBand()

    while True:
        print(f'''
        Choices:
        TASK_1 -> {TASK_1}
        TASK_2 -> {TASK_2}
        EXIT -> {EXIT}
        ---------------------
        ''')
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == TASK_1:
            while True:
                print(f'''
                Choices:
                COUNTRIES_LIST -> {COUNTRIES_LIST}
                ADD_COUNTRY -> {ADD_COUNTRY}
                DEL_COUNTRY -> {DEL_COUNTRY}
                UPDATE_COUNTRY -> {UPDATE_COUNTRY}
                SEARCH_COUNTRY -> {SEARCH_COUNTRY}
                SAVE_DATA -> {SAVE_DATA}
                LOAD_DATA -> {LOAD_DATA}
                EXIT -> {EXIT}
                ---------------------
                ''')

                choice = input('Enter choice: ')
                if choice == EXIT:
                    break

                elif choice == COUNTRIES_LIST:
                    if len(COUNTRIES.get_countries()) > 1:
                        print("\n~~~~~~ Countries ~~~~~~")
                    else:
                        print("\n~~~~~~ Country ~~~~~~")
                    print_result(COUNTRIES.get_countries())

                elif choice == ADD_COUNTRY:
                    country_name = input('Enter the name of the country: ')
                    capital = input('Enter the capital: ')
                    country = COUNTRIES.add_country(
                        country_name = country_name,
                        capital = capital
                    )
                    print("\n~~~~~~ Country ~~~~~~")
                    print_result(country)

                elif choice == DEL_COUNTRY:
                    country_name = input("Enter the name of the country: ")
                    country = COUNTRIES.del_country(country_name = country_name)
                    print("\n~~~~~~ Country ~~~~~~")
                    print_result(country)

                elif choice == UPDATE_COUNTRY:
                    country_name = input("Enter the name of the country: ")
                    country = COUNTRIES.update_country(country_name = country_name)
                    print("\n~~~~~~ Country ~~~~~~")
                    print_result(country)

                elif choice == SEARCH_COUNTRY:
                    country_name = input("Enter the name of the country: ")
                    country = COUNTRIES.search_country(country_name = country_name)
                    print("\n~~~~~~ Country ~~~~~~")
                    print_result(country)

                elif choice == SAVE_DATA:
                    COUNTRIES.save_data()
                    input("Press Enter to continue...")

                elif choice == LOAD_DATA:
                    COUNTRIES.load_data()
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == TASK_2:
            while True:
                print(f'''
                Choices:
                MUSIC_BANDS_LIST -> {MUSIC_BANDS_LIST}
                ADD_MUSIC_BAND -> {ADD_MUSIC_BAND}
                DEL_MUSIC_BAND -> {DEL_MUSIC_BAND}
                UPDATE_MUSIC_BAND -> {UPDATE_MUSIC_BAND}
                SEARCH_MUSIC_BAND -> {SEARCH_MUSIC_BAND}
                SAVE_DATA -> {SAVE_DATA}
                LOAD_DATA -> {LOAD_DATA}
                EXIT -> {EXIT}
                ---------------------
                ''')

                choice = input('Enter choice: ')
                if choice == EXIT:
                    break

                elif choice == MUSIC_BANDS_LIST:
                    if len(MUSIC_BANDS.get_music_bands()) > 1:
                        print("\n~~~~~~ Music bands ~~~~~~")
                    else:
                        print("\n~~~~~~ Music band ~~~~~~")
                    print_result(MUSIC_BANDS.get_music_bands())

                elif choice == ADD_MUSIC_BAND:
                    band_name = input('Enter a name for the music band: ')
                    albums = input('Enter album names with a space: ').split()
                    music_band = MUSIC_BANDS.add_music_band(
                        band_name = band_name,
                        albums = albums
                    )
                    print("\n~~~~~~ Music band ~~~~~~")
                    print_result(music_band)

                elif choice == DEL_MUSIC_BAND:
                    band_name = input('Enter a name for the music band: ')
                    music_band = MUSIC_BANDS.del_music_band(band_name = band_name)
                    print("\n~~~~~~ Music band ~~~~~~")
                    print_result(music_band)

                elif choice == UPDATE_MUSIC_BAND:
                    band_name = input('Enter a name for the music band: ')
                    music_band = MUSIC_BANDS.update_music_band(band_name = band_name)
                    print("\n~~~~~~ Music band ~~~~~~")
                    print_result(music_band)

                elif choice == SEARCH_MUSIC_BAND:
                    band_name = input('Enter a name for the music band: ')
                    music_band = MUSIC_BANDS.search_music_band(band_name = band_name)
                    print("\n~~~~~~ Music band ~~~~~~")
                    print_result(music_band)

                elif choice == SAVE_DATA:
                    MUSIC_BANDS.save_data()
                    input("Press Enter to continue...")

                elif choice == LOAD_DATA:
                    MUSIC_BANDS.load_data()
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")