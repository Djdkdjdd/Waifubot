import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = 2054990632
sudo_users = ["6962772544", "2054990632"]
GROUP_ID = -1002002081714
TOKEN = "6942284208:AAFqGXTASjIkez834A9CJPBGvLiBlSaCPDw"
mongo_url = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://graph.org/file/ecec9ec2082f9c02af8c5.jpg", "https://telegra.ph/file/72ea883532b722f405059.jpg"]
SUPPORT_CHAT = "waifu_support"
UPDATE_CHAT = "dragons_bots"
BOT_USERNAME = "Guess_Yourr_Waifu_bot"
CHARA_CHANNEL_ID = -1002002081714
api_id = 27604779
api_hash = "8a04200c9d52999ae7ebc26a462dbb48"


application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']



