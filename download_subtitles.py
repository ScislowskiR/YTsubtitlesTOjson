# https://www.youtube.com/watch?app=desktop&v=4nzdWXqHEeQ
# https://www.geeksforgeeks.org/python-downloading-captions-from-youtube/
from youtube_transcript_api import YouTubeTranscriptApi
import json
import os
import collections


class DownloadSubtitles:
    def __init__(self, category, video_link, languages, name):
        self.category = category
        self.video_link = video_link
        self.languages = languages
        self.name = name
        self.path = r'D:\pythonProject\YTsubtitlesTOlearningWORDS\YTsubtitlesTOjson\folders' +\
                    '\\' + self.category +\
                    '\\' + self.name + '_' + self.video_link
        self.txt_path = self.path + '.txt'
        self.json_path = self.path + '.json'
        self.srt = YouTubeTranscriptApi.get_transcript(self.video_link, languages=self.languages)

    def subtitles_to_txt(self):
        with open(self.txt_path, 'w+', encoding='utf-8') as f:
            for line in self.srt:
                f.write("{}\n".format(line))

    def subtitles_to_json(self):
        if os.path.isfile(self.json_path) is False:
            with open(self.json_path, 'w+', encoding='utf-8', ) as f:
                json.dump(self.srt, f, ensure_ascii=False)
            self.remake_json(path=self.json_path)

    def remake_json(self, path):
        print(path)
        with open(path, 'r', encoding='utf-8') as j:
            data = json.load(j)
        line_number=0
        for line in data:
            line.pop('duration')
            sentence = collections.defaultdict(list)
            words = line['text'].split()
            word_number = 0
            for word in words:
                sentence[word].append(0)
                sentence[word].append(line_number)
                sentence[word].append(word_number)
                word_number+=1
            line_number+=1
            print(sentence)
            line['text']=sentence
        with open(path, 'w', encoding='utf-8') as j:
            json.dump(data, j, ensure_ascii=False)




if __name__ == '__main__':
    language = "ru"
    language = [language]
    siema = DownloadSubtitles(category=r"russian", video_link="4nzdWXqHEeQ", languages=language, name='Kamczatka')
    siema.subtitles_to_json()
    print('siema1234')
"""
[
  {line1[{w:"...", l:0, c:0}, {w:"...", l:1, c:0}, {w:"...", l:2, c:0}], start, dudration}
  {line2[{w:"...", l:0, c:0}, {w:"...", l:1, c:0}, {w:"...", l:2, c:0}], start, dudration}
  {line3[{w:"...", l:0, c:0}, {w:"...", l:1, c:0}, {w:"...", l:2, c:0}], start, dudration}
  {line4[{w:"",l:0, c:0},{w:"",l:1, c:0},{w:"",l:2, c:0}], start, dudration}
  {line5[{},{},{}], start, dudration}
]
"""
