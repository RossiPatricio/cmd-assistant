import os
from duck_search import *

music_folder = r'C:\Users\PRossi\Music'

def mp3_url(url):
    output_path = fr"{music_folder}\%(title)s.%(ext)s"
    mp3 = f'yt-dlp -x --audio-format mp3 -o {output_path} {url}'
    os.system(mp3)

def mp3_title(title):
    url = get_url(title)
    output_path = fr"{music_folder}\%(title)s.%(ext)s"
    mp3 = f'yt-dlp -x --audio-format mp3 -o {output_path} {url}'
    os.system(mp3)

def video_url(url):
    video = f'yt-dlp -S "res:1080,fps" {url}'
    os.system(video)

def video_title(title):
    url = get_url(title)
    video = f'yt-dlp -S "res:1080,fps" {url}'
    os.system(video)
