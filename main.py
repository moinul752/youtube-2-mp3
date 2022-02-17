from email.mime import base
from pytube import YouTube
import os
print("\nYoutube To Mp3 Format\n")

URL = input("Enter Video URL: ")
yt = YouTube(URL)

try:
    print("\nDwonloading....")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()


    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\nSuccessfully Dwonload\n")

except:
        print("\nSomething Went Wrong! Plese Try Again.....\n")