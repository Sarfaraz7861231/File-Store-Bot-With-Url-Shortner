import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21994708"))
  API_HASH = os.environ.get("API_HASH", "f4a3bd4f38bacd68241866a459c98e30")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7241072993:AAGovFcsTqfTes8NnleSGSm3h9GqSoNDqBM")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "USA_Store_BOT")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "2242848172"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "http://Modijiurl.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "38879ed8def47021329cc25e6594288a7d0c6495")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7096845102"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sarfaztro:a0Bc95DgXRctIZ9W@cluster0.v0gkffl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/+h76NSFWbPsY1OGFk")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "https://t.me/+KMnzHLidB184YWU0"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/@Seller_TOPX})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/KingVj01)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
