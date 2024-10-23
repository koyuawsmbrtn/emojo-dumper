import requests
import os
from dotenv import load_dotenv

instance = os.getenv("INSTANCE")
if not instance:
    raise ValueError("INSTANCE is not set! Make sure the environment variable or .env exists.")
category = os.getenv("CATEGORY")

r = requests.get("https://"+instance+"/api/v1/custom_emojis")
j = r.json()

for item in j:
    if item["visible_in_picker"] == True:
        if category:
            if item["category"] == category:
                extension = item["url"].split(".")[len(item["url"].split(".")) - 1]
                os.system("wget -O "+item["shortcode"]+"."+extension+" "+item["url"])
        else:
            extension = item["url"].split(".")[len(item["url"].split(".")) - 1]
            os.system("wget -O "+item["shortcode"]+"."+extension+" "+item["url"])