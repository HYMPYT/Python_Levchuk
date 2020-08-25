from pickle import load, dump

class MusicBand:
    def __init__(self):
        self.__MUSIC_BANDS = {}

    def add_music_band(self, band_name: str, albums: list) -> dict:
        """This method is for adding music band."""
        self.__MUSIC_BANDS[band_name] = albums
        return {band_name: albums}

    def del_music_band(self, band_name: str) -> dict:
        """This method is for deleting music band.
        The key to the search is the name of the band."""
        if band_name in self.__MUSIC_BANDS.keys():
            return {band_name: self.__MUSIC_BANDS.pop(band_name)}


    def update_music_band(self, band_name: str) -> dict:
        """This method is for editing the music band information fields.
        The key to the search is the name of the band."""
        if band_name in self.__MUSIC_BANDS.keys():
            music_band = {}
            albums = self.__MUSIC_BANDS[band_name]
            new_band_name = input(f"Enter a name for the music band ({band_name} - default): ")
            new_albums = input(f"Enter album names with a space ({albums} - default): ").split()

            if new_albums:
                self.__MUSIC_BANDS[band_name] = new_albums
                music_band[band_name] = new_albums
            if new_band_name:
                self.__MUSIC_BANDS[new_band_name] = self.__MUSIC_BANDS.pop(band_name)
                music_band[new_band_name] = music_band.pop(band_name)
        return music_band

    def search_music_band(self, band_name: str) -> dict:
        """This method for search music band.
        The key to the search is the name of the band."""
        if band_name in self.__MUSIC_BANDS.keys():
            return {band_name: self.__MUSIC_BANDS[band_name]}

    def save_data(self) -> None:
        """This method is for saving data"""
        with open("./music_bands.bin", "wb") as f:
            dump(self.__MUSIC_BANDS, f)

    def load_data(self) -> None:
        """This method is for loading data"""
        with open("./music_bands.bin", "rb") as f:
            self.__MUSIC_BANDS = load(f)

    def get_music_bands(self) -> dict:
        """This method will return the collection __MUSIC_BANDS"""
        return self.__MUSIC_BANDS


if __name__ == "__main__":
    print("This module for importing not for execute.")
