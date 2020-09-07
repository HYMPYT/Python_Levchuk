class Star:
    def __init__(self, name: str, galaxy: str):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return f"~~~~~ Star ~~~~~\nName: {self.name}\nGalaxy: {self.galaxy}"

    def __repr__(self):
        if self.galaxy == 'Milky Way':
            return f"Name: {self.name} Galaxy: {self.galaxy}"
        return f"Another galaxy"

sun = Star('Sun', galaxy='Milky Way')
star_2 = Star('Star 2', galaxy='Another galaxy')
print(sun)