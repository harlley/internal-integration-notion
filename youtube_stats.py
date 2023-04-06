import googleapiclient.discovery


class YoutubeStats:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    def get_video(self, video_id):
        response = self.youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()

        video = response['items'][0]
        view_count = video['statistics']['viewCount']
        like_count = video['statistics']['likeCount']
        comment_count = video['statistics']['commentCount']

        return {
            'view_count': view_count,
            'like_count': like_count,
            'comment_count': comment_count
        }
