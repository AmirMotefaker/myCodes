# Code by amotef@gmail.com

# Youtube Downloader

# Solution 1

from pytube import YouTube
url = 'https://www.youtube.com/watch?v=wHBBoUtJHhA'
yt_video = YouTube(url)

# # here we are fetching a list of all the video resolution
# videos = yt_video.streams.all()
# # we are using enumerate to get the index number
# res_list = list(enumerate(videos))
# for i in res_list:
#     print(i)

# resolution = int(input("Enter the index number of the video : "))
# videos[resolution].download()
# print('your video is downloaded successfully')


# Solution 2 -Basic

# from pytube import YouTube
# YouTube('https://www.youtube.com/watch?v=wHBBoUtJHhA').streams.first().download()
# yt = YouTube('https://www.youtube.com/watch?v=wHBBoUtJHhA')
  
