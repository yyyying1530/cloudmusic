from spyder import CloudMusic

def time(secs):
    secs = secs//1000
    min = secs//60
    sec = secs%60
    if min == 0 :
        result = str(sec)+'秒'
    else:
        result = str(min)+'分'+str(sec)+'秒'
    return result

def analyzeData(data):
    data_list = []
    result = data['result']['songs']
    for i in result:
        buffer = {}
        buffer['歌曲'] = i['name']
        buffer['歌手'] = i['ar'][0]['name']
        buffer['专辑'] = i['al']['name']
        buffer['时长'] = time(i['dt'])
        buffer['id'] = i['id']
        buffer['专辑图片url'] = i['al']['picUrl']

        data_list.append(buffer)
    return data_list

def showData(data):
    print('{:-^97}'.format('搜索结果'))
    print('{0:<5}{1:{5}<20}{2:{5}<15}{3:{5}<10}{4:{5}<20}'.format('序号', '歌曲', '歌手', '时长', '专辑', chr(12288)))
    print('{:-^100}'.format('-'))
    count = 1
    for i in data:

        id = count
        song = i['歌曲']
        singer = i['歌手']
        time = i['时长']
        album = i['专辑']
        print('{0:<5}{1:{5}<20}{2:{5}<15}{3:{5}<10}{4:{5}<20}'.format(id, song, singer, time, album, chr(12288)))

        count = count+1
    print('{:-^100}'.format('-'))
def main():
    name = input('请输入歌名：')
    obj = CloudMusic()
    data = obj.searchbyName(name)
    song_list = analyzeData(data)
    showData(song_list)

    while True:
        try:
            index = int(input('请输入下载的歌曲编号（0代表退出）：'))
            if index==0:
                break
            if index>len(song_list) or index<0:
                print('请输入合法的数字1')
                continue
            obj.download(song_list[index-1])
        except:
            print('请输入合法的数字2')
    pass

def test():
    pass

if __name__ == '__main__':
    main()
    pass
