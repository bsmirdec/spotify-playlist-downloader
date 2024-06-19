import os
from yt_dlp import YoutubeDL

def download_mp3(tracks, destination):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        for track in tracks:
            # Construct the search query
            query = f'ytsearch:"{track["name"]} {track["artist"]}"'
            print(f'Downloadin {track["name"]} - {track["artist"]}...')

            # Perform the search to get the actual file name
            result = ydl.extract_info(query, download=False)
            if 'entries' in result:
                video_info = result['entries'][0]
            else:
                video_info = result

            # Construct the file path based on the expected output template
            file_name = f'{video_info["title"]}.mp3'
            file_path = os.path.join(destination, file_name)
            
            # Print statements for debugging
            print(f'Checking for {file_path}...')

            # Check if the file already exists
            if os.path.exists(file_path):
                print(f'File {file_name} already exists. Skipping download.')
                continue

            # Download the file if it doesn't exist
            ydl.download([query])

            # After download, check if the file was created correctly
            if os.path.exists(file_path):
                print(f'Successfull download: {file_path}')
            else:
                print(f'Error: file {file_path} cannot be found.')
