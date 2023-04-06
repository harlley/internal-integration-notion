import os
from youtube_stats import YoutubeStats
from notion_database import NotionDatabase
from dotenv import load_dotenv

load_dotenv()


def main():
    notion_api_key = os.getenv('NOTION_API_KEY')
    notion_database_id = os.getenv('NOTION_DATABASE_ID')
    youtube_api_key = os.getenv('YOUTUBE_API_KEY')

    notion_db = NotionDatabase(api_key=notion_api_key, database_id=notion_database_id)
    youtube_stats = YoutubeStats(youtube_api_key)

    for row in notion_db.list():
        video_id = row["video_id"]
        stats = youtube_stats.get_video(video_id)
        notion_db.update(page_id=row["page_id"], stats=stats)
        print({"video_id": video_id, "page_id": row["page_id"], "stats": stats})


if __name__ == "__main__":
    main()
