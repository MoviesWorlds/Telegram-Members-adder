import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	ABOUT_BOT_TEXT = f"""
This is Members Adder For Telegram π€!


π€ **My Name:** [Members Adder Bot](https://t.me/{BOT_USERNAME})

π **Platform:** [Python3](https://www.python.org)

π **Library:** [Pyrogram](https://docs.pyrogram.org)

π‘ ** Heroku server:** [Heroku](https://heroku.com)

π§π»βπ» **Editing:** @EverseenMoviesofficial

π₯ **Any Doubt Support group:** [EverseenMovies Group](https://t.me/Everseen_Movies)

π’ **Join My update channel:** [EverseenMovies Channel](http://t.me/+7c2DCEfWueAyMWU1)
"""
	ABOUT_DEV_TEXT = f"""
π§π»βπ» **Developer:** @EverseenMoviesofficial

π²**Donate Now:** @EverseenMoviesofficial

πCreate Any Bot Contact Admin @EverseenMoviesofficial

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Members Adder For Telegram**.

Add Multiple Accounts to Scrap Telegram Group Members **About Bot** Button.
"""
