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

from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=wHBBoUtJHhA').streams.first().download()
