import requests
import json


class NotionDatabase:

    def __init__(self, api_key: str, database_id: str):
        self.database_id = database_id
        self.headers = {
            "Notion-Version": "2021-08-16",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def list(self):
        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"

        response = requests.post(url, headers=self.headers)

        data = []

        for result in response.json()["results"]:
            page_id = result["id"]
            url = result["properties"]["URL"]["url"]
            if url is not None:
                video_id = url.split("v=")[1]
                data.append({"video_id": video_id, "page_id": page_id})

        return data

    def update(self, page_id, stats):
        payload = {
            "properties": {
                "Yt Views": {
                    "number": int(stats["view_count"])
                },
                "Likes": {
                    "number": int(stats["like_count"])
                },
                "Comments": {
                    "number": int(stats["comment_count"])
                }
            }
        }

        url = f"https://api.notion.com/v1/pages/{page_id}"

        response = requests.patch(url, headers=self.headers, data=json.dumps(payload))

        if response.status_code == 200:
            print("Youtube stats updated successfully!")
        else:
            print(f"Failed to update page. Error code: {response.status_code}")
