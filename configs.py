# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27157998"))
    API_HASH = getenv("API_HASH", "45d09c93e37c9b93b6535949c898f906")
    BOT_TOKEN = getenv("BOT_TOKEN", "6887853132:AAFCe_b5C4hu87J6pVeJnTagazzGsRoI8E0")
    FSUB = getenv("FSUB", "Ghost_Botz")
    CHID = int(getenv("CHID", "-1002143564040"))
    SUDO = list(map(int, getenv("SUDO", "1452198353").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
