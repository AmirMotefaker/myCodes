# Code by @AmirMotefaker

# Instagram Bot (with InstaBot)

# pip install instabot
# instabot: Instagram bot scripts for promotion and API python wrapper.


## Login
# Import instabot library
from instabot import Bot
 
bot = Bot()
 
# Login
bot.login(username="your_userid",
          password="your_password")


## Follow
# To follow single person.
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
# Follow
bot.follow("iThinker_bot")

# To follow more person.
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
list_of_user = ["user_id1", "user_id2", "user_id3", "...."]
bot.follow_users(list_of_user)


## Unfollow
# To unfollow a single person.
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
bot.unfollow("iThinker_bot")

# To unfollow more person.
from instabot import Bot
 
bot = Bot()
bot.login(username = "your_username",
          password = "your_password")
 
unfollow_list = ["user_id1", "user_id2", "user_id3", "..."]
bot.unfollow_users(unfollow_list)


## Unfollow everyone
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
# Unfollow everyone!
bot.unfollow_everyone()


## Count the number of followers
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
# Count number of followers
followers = bot.get_user_followers("geeks_for_geeks")
print("Total number of followers:")
print(len(followers))


## Send messages
# To send message to a single person.
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
message = "I like iThinker"
bot.send_message(message, "iThinker_bot")

# To send same message to many follower.
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
message = "I like iThinker"
list_of_userid = ["user_id1", "user_id2", "user_id3", "..."]
bot.send_messages(message, list_of_userid)


## Send Like messages
# To send like to one or more person.
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
send_like_list = ["user_id1", "user_id2", "user_id3", "..."]
bot.send_like(send_like_list)


## Post Photo
from instabot import Bot
 
bot = Bot()
bot.login(username="your_username",
          password="your_password")
 
# Post photos
# Photos need be resized and, if not in ratio given below.
# jpg format works more better than others formats.
# Acceptable Ratio of image:-  90:47, 4:5, 1:1(square image).
# Keep image and program in same folder.
# -----------------------------------------------------------
bot.upload_photo("filename.jpg", caption="Write caption here.")

