import os

home = os.path.dirname(os.path.realpath(__file__))


def Download_vtt(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        urls = f.readlines()
        for i, url in enumerate(urls):
            print(i)
            os.system('youtube-dl --write-auto-sub --skip-download '+url)
    vtt2srt()


def vtt2srt():
    files = []
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(home):
        # for dirname in dirnames:                           #输出文件夹信息
        #     print("parent is:" + parent)
        #     print("dirname is" + dirname)

        for filename in filenames:                          #输出文件信息
            # print("filename is:" + filename)
            if(len(filename)>3 and filename[-3:]=="vtt"):
                files.append(filename)
    for filename in files:
        os.system('ffmpeg -i "'+home+'/'+filename+'" "'+home+'/'+filename[:-3]+'srt"')


if __name__=="__main__":
    Download_vtt("urls.txt")
    print("finish")
