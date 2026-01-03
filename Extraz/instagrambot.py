from instabot import Bot as InstaBot

bot = InstaBot()
bot.login(username="", password="") # use yours

# operations >> 
bot.follow("username")
bot.upload_photo("pic path ", caption ="")
bot.upload_video("",caption="")
bot.unfollow("username")
bot.unfollow_everyone()
bot.follow_following()



bot.get_comment()
bot.get_messages()
bot.get_pending_follow_requests()