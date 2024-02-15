import os
import logging

from googleapiclient.discovery import build
from dotenv import load_dotenv
from ..utils.logger import set_logger

load_dotenv()

class YouTubeAPI:

    def __init__(self):
        self.logger = set_logger(__name__)
        self.api_key = os.getenv("YOUTUBE_KEY")
        self.api_service_name = "youtube"
        self.api_vesion = "v3"

        self.youtube = build(self.api_service_name, self.api_vesion, developerKey=self.api_key)
        self.logger.info("YouTube API initialized")
    
    def get_captions(self, video_id):
        self.logger.debug("Fetching captions data")
        request = self.youtube.captions().list(
            part="snippet",
            videoId=video_id
        )
        response = request.execute()
        self.logger.info("Captions data fetched successfully")
        return response