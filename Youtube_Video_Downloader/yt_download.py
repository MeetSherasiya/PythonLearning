from pytube import YouTube
from sys import argv

url = ''
my_video = YouTube(url)

print(my_video.title)

my_video = my_video.streams.get_highest_resolution()

my_video.download('/Users/Jigu/Documents/GitHub/PythonLearning/Youtube_Video_Downloader')