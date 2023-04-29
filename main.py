import yt_dlp
import urllib.request
import time
import os

# Check for internet connectivity and print connection speed
try:
    start_time = time.time()
    urllib.request.urlopen('http://google.com')
    end_time = time.time()
    print(f"Internet connection speed: {round((end_time - start_time) * 1000)} ms")
except:
    print("No internet connection. Aborting script.")
    exit()

# Get the YouTube video URL from the user
url = input("Enter the YouTube video URL: ")

# Create a directory to store the downloaded videos
if not os.path.exists('downloaded-videos'):
    os.makedirs('downloaded-videos')

# Set options for yt-dlp
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': 'downloaded-videos/%(title)s.%(ext)s',
}

try:
    # Create a yt-dlp object and download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Video downloaded successfully.")

except Exception as e:
    print("An error occurred while downloading the video:")
    print(str(e))
