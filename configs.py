import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	ABOUT_BOT_TEXT = f"""
This is Members Adder For Telegram 🤖!


🤖 **My Name:** [Members Adder Bot](https://t.me/{BOT_USERNAME})

📝 **Platform:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 ** Heroku server:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Editing:** @EverseenMoviesofficial

👥 **Any Doubt Support group:** [EverseenMovies Group](https://t.me/Everseen_Movies)

📢 **Join My update channel:** [EverseenMovies Channel](http://t.me/+7c2DCEfWueAyMWU1)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @EverseenMoviesofficial

💲**Donate Now:** @EverseenMoviesofficial

📌Create Any Bot Contact Admin @EverseenMoviesofficial

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Members Adder For Telegram**.

Add Multiple Accounts to Scrap Telegram Group Members **About Bot** Button.
"""
