from spd.models.spotify_api import SpotifyAPI
from spd.views.main_view import MainView
from spd.utils.downloader import download_mp3

class MainController:
    def __init__(self):
        self.model = SpotifyAPI()
        self.view = MainView(self)

    def run(self):
        self.view.mainloop()

    def download_playlist(self, url, destination):
        playlist = self.model.get_playlist(url)
        download_mp3(playlist, destination)

    def get_playlist(self, url):
        playlist = self.model.get_playlist(url)
        return playlist
