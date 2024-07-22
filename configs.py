import os

class Config(object):
    API_ID = int(os.environ.get("20478027", ""))
    API_HASH = os.environ.get("6ec1282bf0a6ef76dd4141bc32f93dcd", "")
    BOT_TOKEN = os.environ.get("7249121269:AAEJDKJsxffBR4YQSnRr8FRVbKODfqmRh5Y", "")
    BOT_USERNAME = os.environ.get("SAXXSUXXbot", "")
    DB_CHANNEL = int(os.environ.get("-1002208519546", ""))
    SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "vnshortener.com")
    SHORTLINK_API = os.environ.get('SHORTLINK_API', "2c5ffd5d9400ea9d263b308f53c315acc227f486")
    BOT_OWNER = int(os.environ.get("7208155074", ""))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
    OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
    ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send me any media or file, and I will store it permanently. I can also work in channels; add me with edit permissions, and I will save uploaded files in the channel and share a shareable link.

To access this bot for 24 hours, please complete a task using the link shortener below:

[Complete Task]({SHORTLINK_URL})

╭────[ 🔅FileStoreBot🔅 ]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
╰──────[ 😎 ]───────────⍟
"""
    ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 Developer: [VJ](https://telegram.me/KingVj01)
 
I am a super noob. Please support my hard work.

[Donate Me](https://t.me/KingVj01)
"""
    HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

To use this bot and benefit from its features, please complete the link shortener task to gain 24-hour access:

[Complete Task]({SHORTLINK_URL})

Benefits:
- Send me any file, and it will be uploaded to my database, providing you with a permanent file link.
- Ideal for Telegram movie channels or any copyright channels to avoid infringement issues.

**About Bot**:

- Send me your file, and I will provide a permanent link to keep your channel safe from copyright infringement issues.
- I support channels too.
"""
