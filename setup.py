from setuptools import setup, find_packages

setup(
    name="spotify-playlist-downloader",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "spotipy",
        "youtube_dl",
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "spotify-playlist-downloader = my_project.app:main",
        ],
    },
)
