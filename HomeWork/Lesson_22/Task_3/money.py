from math import modf


class Money:
    """This class contains information about the Money.
        Class object operates with one currency."""

    _UAH = -1.0
    _USD = -1.0
    _EUR = -1.0
    _RUB = -1.0

    def __init__(self, *, UAH: float = -1.0, USD: float = -1.0, EUR: float = -1.0, RUB: float = -1.0):
        """Initialize the object of money"""
        if not UAH == -1.0:
            self.UAH = UAH

        if not RUB == -1.0:
            self.RUB = RUB

        if not USD == -1.0:
            self.USD = USD

        if not EUR == -1.0:
            self.EUR = EUR

    @property
    def UAH(self) -> str:
        """Returns a representation of the UAH"""
        return f"UAH: {Money._UAH}.{self._UAH_kopeck}"
    
    @UAH.setter
    def UAH(self, value: float):
        """Sets the value in the _UAH and the _UAH_kopeck fields"""
        if Money._USD < 0 and Money._EUR < 0 and Money._RUB < 0 and value:
            try:
                value = float(value)
                if value >= 0.0:
                    Money._UAH = int(modf(value)[1])
                    self._UAH_kopeck = int(round(modf(value)[0], 2) * 100)
                else:
                    raise ValueError("value must be positive")
            except ValueError as e:
                print(f"Error: {e}")
        elif not value == -1.0:
            print("This object works with another currency")
    
    def __set_UAH_kopeck(self, value: int):
        """Sets the value in the _UAH_kopeck field"""
        if value:
            try:
                kopeck = int(value)
                if kopeck >= 0:
                    Money._UAH += kopeck // 100
                    self._UAH_kopeck = kopeck - (kopeck // 100) * 100
                else:
                    raise ValueError("Field of the kopeck must be positive")
            except ValueError as e:
                print(f"Error: {e}")

    # Setter
    UAH_kopeck = property(fset=__set_UAH_kopeck)

    @property
    def USD(self) -> str:
        """Returns a representation of the USD"""
        return f"USD: {Money._USD}.{self._USD_cent}"

    @USD.setter
    def USD(self, value: float):
        """Sets the value in the _USD and the _USD_cent fields"""
        if Money._UAH < 0 and Money._EUR < 0 and Money._RUB < 0 and value:
            try:
                value = float(value)
                if value >= 0.0:
                    Money._USD = int(modf(value)[1])
                    self._USD_cent = int(round(modf(value)[0], 2) * 100)
                else:
                    raise ValueError("value must be positive")
            except ValueError as e:
                print(f"Error: {e}")
        elif not value == -1.0:
            print("This object works with another currency")

    def __set_USD_cent(self, value: int):
        """Sets the value in the  _USD_cent field"""
        if value:
            try:
                cent = int(value)
                if cent >= 0:
                    Money._USD += cent // 100
                    self._USD_cent = cent - (cent // 100) * 100
                else:
                    raise ValueError("Field of the usd cent must be positive")
            except ValueError as e:
                print(f"Error: {e}")

    # Setter
    USD_cent = property(fset=__set_USD_cent)

    @property
    def EUR(self) -> str:
        """Returns a representation of the EUR"""
        return f"EUR: {Money._EUR}.{self._EUR_cent}"

    @EUR.setter
    def EUR(self, value: float):
        """Sets the value in the _EUR and the _EUR_cent fields"""
        if Money._UAH < 0 and Money._USD < 0 and Money._RUB < 0 and value:
            try:
                value = float(value)
                if value >= 0.0:
                    Money._EUR = int(modf(value)[1])
                    self._EUR_cent = int(round(modf(value)[0], 2) * 100)
                else:
                    raise ValueError("value must be positive")
            except ValueError as e:
                print(f"Error: {e}")
        elif not value == -1.0:
            print("This object works with another currency")

    def __set_EUR_cent(self, value: int):
        """Sets the value in the _EUR_cent field"""
        if value:
            try:
                cent = int(value)
                if cent >= 0:
                    Money._EUR += cent // 100
                    self._EUR_cent = cent - (cent // 100) * 100
                else:
                    raise ValueError("Field of the eur cent must be positive")
            except ValueError as e:
                print(f"Error: {e}")

    # Setter
    EUR_cent = property(fset=__set_EUR_cent)

    @property
    def RUB(self) -> str:
        """Returns a representation of the RUB"""
        return f"RUB: {Money._RUB}.{self._RUB_kopeck}"

    @RUB.setter
    def RUB(self, value: float):
        """Sets the value in the _RUB and the _RUB_kopeck fields"""
        if Money._UAH < 0 and Money._USD < 0 and Money._EUR < 0 and value:
            try:
                value = float(value)
                if value >= 0.0:
                    Money._RUB = int(modf(value)[1])
                    self._RUB_kopeck = int(round(modf(value)[0], 2) * 100)
                else:
                    raise ValueError("value must be positive")
            except ValueError as e:
                print(f"Error: {e}")
        elif not value == -1.0:
            print("This object works with another currency")

    def __set_RUB_kopeck(self, value: int):
        """Sets the value in the _RUB_kopeck field"""
        if value:
            try:
                kopeck = int(value)
                if kopeck >= 0:
                    Money._RUB += kopeck // 100
                    self._RUB_kopeck = kopeck - (kopeck // 100) * 100
                else:
                    raise ValueError("Field of the kopeck must be positive")
            except ValueError as e:
                print(f"Error: {e}")

    # Setter
    RUB_kopeck = property(fset=__set_RUB_kopeck)

    def __del__(self):
        """Destructor"""
        Money._UAH = -1.0
        Money._RUB = -1.0
        Money._USD = -1.0
        Money._EUR = -1.0



if __name__ == "__main__":
    print("This module for import not for execute!")