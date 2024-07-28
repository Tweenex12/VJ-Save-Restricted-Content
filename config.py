import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23263522"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "41aa1eab83b88e7af40346744ebdac07")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vaishalix12:znUPWtET9GOe13hP@cluster0.vwtj0ll.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
