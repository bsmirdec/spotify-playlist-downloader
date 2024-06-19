import tkinter as tk
from tkinter import filedialog
import os
import sys

IS_BUNDLED = hasattr(sys, "_MEIPASS")
BUNDLE_DIR = getattr(
    sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))
)

IMAGE_PATH = "cat.png"

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # self.geometry("450x600")
        
        self.background_color = "#0f1927"
        self.text_color = "#71eff9"
        self.title("Spotify Playlist Downloader")
        self['bg'] = self.background_color

        tk.Label(self, text="Spotify playlist URL :", font=("Verdana", 24, "italic bold"), fg=self.text_color, bg=self.background_color).pack(pady=10)
        self.url_entry = tk.Entry(self, width=50, bg=self.background_color, fg="white", highlightbackground="#e04cb7", highlightcolor=self.text_color)
        self.url_entry.pack(padx=10)

        self.download_button = tk.Button(self, text="Browse folder", borderwidth=0, font=("Verdana", 16), highlightbackground=self.text_color, background=self.background_color, command=self.download_playlist)
        self.download_button.pack(pady=10)

        image_path = os.path.abspath(os.path.join(BUNDLE_DIR, IMAGE_PATH))
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(2) 
        tk.Label(self, image=self.image, borderwidth=0).pack()

    def download_playlist(self):
        playlist_url = self.url_entry.get()
        destination_folder = filedialog.askdirectory()
        if playlist_url and destination_folder:
            self.controller.download_playlist(playlist_url, destination_folder)

