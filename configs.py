# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "1859341"))
    API_HASH = getenv("API_HASH", "8d1de558964d482b32b9b65d0e2c5377")
    BOT_TOKEN = getenv("BOT_TOKEN", "6799250953:AAF3WsUC9gFfO_R6USYG42rxzzNCyw_r3nQ")
    FSUB = getenv("FSUB", "billabombay")
    CHID = int(getenv("CHID", "-1001742846530"))
    SUDO = list(map(int, getenv("SUDO", "5777436923").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://mathewmaxton:4PLBCZ4xhxlYB7II@cluster0.udnd6vl.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
