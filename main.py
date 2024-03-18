from pytube import YouTube
import os
import shutil



# Get the YouTube video URL from user input
video_url = input("Enter the URL of the video you want to download: \n>>")
yt = YouTube(video_url)

# Filter for the audio stream
audio = yt.streams.filter(only_audio=True).first()

# Prompt user for destination directory
destination = input("Enter the destination (leave blank for current directory):\n") or '.'

# If the destination is not the current directory, create a folder with the provided name
if destination != '.':
    # Create directory if it doesn't exist
    os.makedirs(destination, exist_ok=True)

# Download the audio
out_file = audio.download(output_path=destination)

# Extract the file name from the path
file_name = os.path.basename(out_file)


# Rename the downloaded file to have a .mp3 extension
base, _ = os.path.splitext(file_name)
new_file = os.path.join(destination, base + '.mp3')
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded in .mp3 format.")
