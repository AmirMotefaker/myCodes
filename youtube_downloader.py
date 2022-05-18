# Code by amotef@gmail.com

# Youtube Downloader

# Solution 1 - BEST

# from pytube import YouTube
# url = 'https://www.youtube.com/watch?v=wHBBoUtJHhA'
# yt_video = YouTube(url)

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
  

# Solution 3 

# from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=wHBBoUtJHhA')
# yt.streams.get_highest_resolution().download()



# Solution 4 - video description

# from pytube import YouTube

# video = YouTube("https://www.youtube.com/watch?v=wHBBoUtJHhA")
# print (video.description)


# Solution 5 - advanced 

# from pytube import YouTube

# def get_stream_for_res(streams, res):
#     stream = list(filter(lambda x: x.resolution == res, streams))
#     return stream

# video_url = input("Enter YouTube Video URL: ").strip()
# youtube_obj = YouTube(video_url)

# video_res = input(f"Enter YouTube Video Resolution for {youtube_obj.title}: ").strip()
# req_stream_obj = get_stream_for_res(youtube_obj.streams, video_res)[0]

# req_stream_obj.download()
# print(f"YouTube Video {youtube_obj.title} Downloaded With Resolution {video_res}")


# Solution 6 - fastest way to download a Youtube video with Python

# from pytube import YouTube
# YouTube('https://www.youtube.com/watch?v=wHBBoUtJHhA').streams.first().download()


# Solution 7 - with API

from tkinter import *
from pytube import YouTube

# Create Display Window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouYube Video Downloader - Amir Motefaker -")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

# Create Field to Enter Link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

# Create Function to Start Downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()
