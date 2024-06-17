import tkinter as tk
from tkinter import filedialog

background_color = "#1ed660"

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Téléchargement de Playlist Spotify")
        
        self['bg'] = background_color

        tk.Label(self, text="URL de la playlist Spotify :").pack()
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack()

        self.infos_button = tk.Button(self, text="Infos playlist", command=self.get_playlist)
        self.infos_button.pack()

        self.download_button = tk.Button(self, text="Sélectionner le dossier de destination", command=self.download_playlist)
        self.download_button.pack()
    
    def get_playlist(self):
        playlist_url = self.url_entry.get()
        playlist = self.controller.get_playlist(playlist_url)
        for track in playlist:
            tk.Label(self, text=f"Titre : {track["name"]}, Artist : {track["artist"]}").pack()

    def download_playlist(self):
        playlist_url = self.url_entry.get()
        destination_folder = filedialog.askdirectory()
        if playlist_url and destination_folder:
            self.controller.download_playlist(playlist_url, destination_folder)

