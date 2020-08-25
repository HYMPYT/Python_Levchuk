from pickle import load, dump

class Country:
    def __init__(self):
        self._COUNTRIES = {}

    def add_country(self, country_name: str, capital: str) -> dict:
        """This function is for adding country."""
        self._COUNTRIES[country_name] = capital
        return {country_name: capital}

    def del_country(self, country_name: str) -> dict:
        """This function is for deleting country.
        The key to the search is the name of the country."""
        if country_name in self._COUNTRIES.keys():
            return {country_name: self._COUNTRIES.pop(country_name)}

    def update_country(self, country_name: str) -> dict:
        """This function is for editing the country information fields.
        The key to the search is the name of the country."""
        if country_name in self._COUNTRIES.keys():
            country = {}
            capital = self._COUNTRIES[country_name]
            new_country_name = input(f"Enter the name of the country ({country_name} - default): ")
            new_capital = input(f"Enter the capital ({capital} - default): ")

            if new_capital:
                self._COUNTRIES[country_name] = new_capital
                country[country_name] = new_capital
            if new_country_name:
                self._COUNTRIES[new_country_name] = self._COUNTRIES.pop(country_name)
                country[new_country_name] = country.pop(country_name)
        return country

    def search_country(self, country_name: str) -> dict:
        """This function for search country.
        The key to the search is the name of the country."""
        if country_name in self._COUNTRIES.keys():
            return {country_name: self._COUNTRIES[country_name]}

    def save_data(self) -> None:
        """This function is for saving data"""
        with open("./countries.bin", "wb") as f:
            dump(self._COUNTRIES, f)

    def load_data(self) -> None:
        """This function is for loading data"""
        with open("./countries.bin", "rb") as f:
            self._COUNTRIES = load(f)


if __name__ == "__main__":
    print("This module for importing not for execute.")
