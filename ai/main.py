from ai.utils.logger import set_logger
from ai.api.youtube_api import YouTubeAPI

def main():

    logger = set_logger(__name__)
    logger.info("Program started")

    youtube = YouTubeAPI()
    print(youtube.get_captions("qqrpMRDuPfc"))    
 
if __name__ == "__main__":
    main()
