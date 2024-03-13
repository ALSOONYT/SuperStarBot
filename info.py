# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '20389440'))
API_HASH = environ.get('API_HASH', 'a1a06a18eb9153e9dbd447cfd5da2457')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/ebad2eb29a3d2702e1531.jpg https://telegra.ph/file/5250452a1ab5364cfc4dc.jpg https://telegra.ph/file/68a707b00e8e88ed3c4a4.jpg https://telegra.ph/file/f44b3f7381cbf2e7708bb.jpg https://telegra.ph/file/4aaa6122c1fe3b71cf52c.jpg https://telegra.ph/file/486a9c2e80ed1729a345f.jpg https://telegra.ph/file/b165f958d038b903d43e1.jpg https://telegra.ph/file/989a744a60c061838444f.jpg https://telegra.ph/file/ff8f67820985179067982.jpg https://telegra.ph/file/3d8c714a3b0c04bfdec7e.jpg https://telegra.ph/file/fd0e1a19b0268c005edf8.jpg https://telegra.ph/file/8cfe0b5ceaa7b969448c4.jpg https://telegra.ph/file/5965fb86394de52b45e31.jpg https://telegra.ph/file/b826e4fabf1bf0fa72db3.jpg https://telegra.ph/file/baba127a57d74bc19e956.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/a27dc8fe434e6b846b0f8.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/How_To_Open_Linkl")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6168162777').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001722984461').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "vkbotsthalpathy")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'moneykamalo.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '0eefb93e1e3ce9470a7033115ceb1bad13a9d674')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/vj_bot_disscussion')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/vj_bots')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_To_Open_Linkl')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends ❤️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001623633000'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'vj_bot_disscussion')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]
