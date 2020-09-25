import requests
from encrypt import Encrypt
import os

class CloudMusic:
    def __init__(self):

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def searchbyName(self, name):
        encrypt = Encrypt()
        text_dir = {
            "hlpretag": "<span class=\"s-fc7\">",
            "hlposttag": "</span>",
            "s": name,
            "type": "1",
            "offset": "0",
            "total": "true",
            "limit": "30",
            "csrf_token": ""
        }
        text = str(text_dir)
        data = encrypt.getParamsAndSecKey(text)
        searchUrl = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        try:
            response = requests.post(url=searchUrl, data=data, headers=self.headers)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.json()
        except Exception as err:
            print(err)
            return '请求异常'

    def download(self, song):
        id = song['id']
        result = self.download_search(str(id))
        download_url = result['data'][0]['url']
        self.saveFile(song, download_url)

    def download_search(self, id):
        encrypt = Encrypt()
        text_dir = {
            "ids":"["+id+"]",
            "level":"standard",
            "encodeType":"aac",
            "csrf_token":""
        }
        id_url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
        text = str(text_dir)
        data = encrypt.getParamsAndSecKey(text)
        try:
            response = requests.post(url=id_url, data=data, headers=self.headers)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.json()
        except Exception as err:
            print(err)
            return '请求异常'

    def saveFile(self, song, url):
        filepath = './download'
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        song_name = song['歌曲']
        singer = song['歌手']
        filename = song_name+'-'+singer
        response = requests.get(url, headers=self.headers)
        with open(os.path.join(filepath, filename) + '.mp3', 'wb') as f:
            f.write(response.content)
            print("下载完毕!")

def test():
    pass

if __name__ == '__main__':
    test()
    pass