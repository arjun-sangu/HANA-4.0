# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "𝙼𝚄𝙷𝙰𝙼𝙼𝙴𝙳")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "PR0FESS0_99")

# Account
API_HASH = "b8b78728c7f08859bfa98f5cbb250dc8" #os.environ.get("API_HASH", "5b1d0662294a21cb54555a4fafeb0c88")
API_ID = 18988485 #os.environ.get("API_ID", "6170856")
# About Bot
BOT_TOKEN = "5392550336:AAFaUaKQjUCdzhnh6PHoKLDwqZwZ7417Evo" #os.environ.get("BOT_TOKEN", "1905228806:AAH2iSgFcg5J6bqpcW11jB93wHbIOJslGTY")
PICS = os.environ.get("PICS", "https://telegra.ph/file/034d53b5ed1d920ecab8b.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Gofilearjun")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://1:1@cluster0.7tlwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Chats & Users
ADMINS = [5036474012] #os.environ.get("ADMINS", "2028425293 1637186875")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Mo_Tech_Group")
AUTH_CHANNEL = -1001610770597 #os.environ.get("AUTH_CHANNEL", "-1001685151224")
CHANNELS = [-1001610770597 -1001610770597] #[int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001784382279").split()]
LOG_CHANNEL = -1001610770597 #os.environ.get("LOG_CHANNEL", "-1001590063851")
GET_FILECHANNEL = -1001508009316 #os.environ.get("GET_FILECHANNEL", "-1001570208190")

# AutoFilter
AUTH_GROUPS = -1001750271875 # os.environ.get("AUTH_GROUPS", "")
AUTH_USERS = [5036474012] #[int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 
