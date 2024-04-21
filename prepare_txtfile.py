# https://www.youtube.com/watch?app=desktop&v=4nzdWXqHEeQ
# https://www.geeksforgeeks.org/python-downloading-captions-from-youtube/
from youtube_transcript_api import YouTubeTranscriptApi


class DownloadSubtitles:
    def __init__(self, video_link):
        self.video_link = video_link
        self.text_path = r'D:\pythonProject\YTsubtitlesTOlearningWORDS\\' + self.video_link + '.txt'
        srt = YouTubeTranscriptApi.get_transcript(self.video_link, languages=['ru'])
        # print(srt)
        with open(self.text_path, 'w+', encoding='utf-8') as f:
            f.write("{}\n".format(srt[0]))
            for line in srt:
                f.write("{}\n".format(line))


if __name__ == '__main__':
    DownloadSubtitles(video_link="4nzdWXqHEeQ")
