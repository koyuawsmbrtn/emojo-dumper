import os
import requests
from dotenv import load_dotenv

access_token = os.getenv("ACCESS_TOKEN")
instance = os.getenv("INSTANCE")
if not instance:
    raise ValueError("INSTANCE is not set! Make sure the environment variable or .env exists.")
if not access_token:
    raise ValueError("ACCESS_TOKEN is not set! Make sure the environment variable or .env exists.")

url = "https://"+instance+"/api/v1/admin/custom_emojis"

directory = "."

for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".gif") or filename.endswith(".webp"):
        file_path = os.path.join(directory, filename)
        shortcode = os.path.splitext(filename)[0]
        filetype = filename.split(".")[len(filename.split(".")) - 1]
        with open(file_path, 'rb') as image_file:
            files = {'image': (filename, image_file, 'image/'+filetype)}
            data = {'shortcode': shortcode}
            headers = {
                'Authorization': f'Bearer {access_token}'
            }
            response = requests.post(url, headers=headers, files=files, data=data)
            if response.status_code == 200:
                print(f"Successfully uploaded: {filename}")
            else:
                print(f"Error uploading {filename}: {response.status_code} - {response.text}")
