# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27157998"))
    API_HASH = getenv("API_HASH", "45d09c93e37c9b93b6535949c898f906")
    BOT_TOKEN = getenv("BOT_TOKEN", "6806956662:AAGArlL9k0cQQqeDE4feCXzGnHHe4PN9FsY")
    FSUB = getenv("FSUB", "Ghost_Botz")
    CHID = int(getenv("CHID", "-1002143564040"))
    SUDO = list(map(int, getenv("SUDO", "1452198353").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Closter0:kkiinngg123@cluster0.wpgtvxh.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
