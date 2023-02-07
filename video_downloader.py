import youtube_dl

ydl_opts = {}

url = input("Enter the url of the video you want to download: ")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
