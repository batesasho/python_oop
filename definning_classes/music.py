class Music:
    def __init__(self, title, artist, lyrics):
        self.lyrics = lyrics
        self.title = title
        self.artist = artist

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
