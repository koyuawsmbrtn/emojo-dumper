import requests
import os

r = requests.get("https://mastodon.de/api/v1/custom_emojis")
j = r.json()

for item in j:
    if item["visible_in_picker"] == True:
        extension = item["url"].split(".")[len(item["url"].split(".")) - 1]
        os.system("wget -O "+item["shortcode"]+"."+extension+" "+item["url"])
