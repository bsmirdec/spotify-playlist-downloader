import subprocess

def download_mp3(tracks, destination):
    for track in tracks:
        query = f"yt-dlp -x --audio-format mp3 --audio-quality 0 ytsearch:\"{track["name"]} {track["artist"]}\" -o \"{destination}/%(title)s.%(ext)s\""
        subprocess.run(query, shell=True)