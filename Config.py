import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("5066680346:AAGGjOUEFSFBPrxAUTnHNwUr34i72ildYRU", None)
    STRING_SESSION = os.environ.get("1BVtsOJ8Bu7xxM23tmtuY2s2yKaSyXZ8HeuwTVZcTVWm2iU425XzlFnv2s761CzaYOGJkG0seL8ai1C4iiLTkZ3nmubNodZXtCYvjgH9hV__N1SJuejnb0I6pmCSnbW9zYylKV7YxdLGuOkCRoaL43mE_l_YfocBeasA5Hup9mSxLueaGQaVbeb6JdQC8h49QQ4xQ3NqHEjlz-5VGz-TAZXYSnvY4pgo4CmT7AxkZyO6KZDn1sJImXkDxEJfaaq_sr195dr945duxHi7FindvRFpMzMbVTHASgJ9NSdLilnTUIECl8TrA2aMAM7qNYe4NpZ2wqU8zI32QoYqLPW1ynOKTV6-IPhc=", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
