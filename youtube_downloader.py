from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
# plots

import matplotlib.pyplot as plt

# image operation
import cv2

url = input("Enter the youtube URL you want to download ")
#video = YouTube('https://www.youtube.com/watch?v=vT3GUKuAzIs')
video = YouTube(url)
video.streams.all()

print(video.streams.filter(file_extension = "mp4").all())

selected_stream =  input("Enter the itag number you want to download ")

video.streams.get_by_itag(selected_stream).download()