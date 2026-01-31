# (c) @AbirHasan2005

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("8364856533:AAGyZGaoe5nRiDxMcg9-yWvohYefo9a4lTM")
	API_ID = int(os.environ.get("39857913", 12345))
	API_HASH = os.environ.get("61b6cc97b562a773634defb8ca5688c6")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get(" -1003829742176"))
	UPDATES_CHANNEL = os.environ.get("-1003685810251", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("7781286450", 1445283714))
	CAPTION = "By @AHToolsBot"
	BOT_USERNAME = os.environ.get("watermarkaddewr_bot", "VideoWatermark_Bot")
	DATABASE_URL = os.environ.get("mongodb+srv://valok35926_db_user:aCJTfDtsuQwEb70Q@cluster0.6z9bunt.mongodb.net/?appName=Cluster0")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", False))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/linux_repo).__

Desgined by @AbirHasan2005
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
