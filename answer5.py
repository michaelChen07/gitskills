# encoding=utf-8

# 要求：批量抓取煎蛋网妹子栏目下的图片（http://jandan.net/ooxx）

import urllib
import re , os

# 定义一个getHtml()函数
def getHtml(url):
    page = urllib.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read() # read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'   #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法获取html中包含 imgre（正则表达式）的数据列表
    #print imglist
    return imglist

def download(imglist,num = None):
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    # num可设置抓取图片的数量

    if not os.path.exists("picture"):  # 判断存放图片的picture文件夹是否存在，不存在则先创建
        os.mkdir("picture")

    x = 1
    for imgurl in imglist[:num]:
        if "http:" in imgurl:
            urllib.urlretrieve(imgurl,'picture/%s.jpg' % x)
        else:
            urllib.urlretrieve("http:"+imgurl, 'picture/%s.jpg' % x)
        x += 1
    print "finished!"

url = "http://jandan.net/ooxx"
html = getHtml(url) # 获得url指向的html内容
imageList = getImg(html)#获得所有图片的地址，返回列表
download(imageList)#下载所有的图片
