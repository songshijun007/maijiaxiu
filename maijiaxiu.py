import urllib.request,socket,re,sys,os

targetPath = "D:/spider/maijiaxiu/images"#注意更改你锁需要存放的路径，否则会报错

def saveFile(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    return t

def data(url):
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/60.0.3112.113 Safari/537.36'
               }

    request = urllib.request.Request(url = url)

    response = urllib.request.urlopen(request)

    data = response.read().decode('utf-8')

    return data

def pagenumber(url):
    data1 = data(url)

    reg = re.compile(r'<div class="pagebar">.*?<span class="dots">.*?<a.*?title="第(.*?)页"')

    number = re.findall(reg,data1)

    print(number[0])

    return number[0]

def findpictures(url):
    data2 = data(url)
    
    reg = re.compile(r'<div class="thumb">.*?<a href.*?_blank.*?<img src="(.*?)".*?</a>',re.S)

    items = re.findall(reg,data2)

    print (items)

    return items

for p in range(1,int(pagenumber("http://www.qipamaijia.com/fuli/"))):
    for link in findpictures("http://www.qipamaijia.com/fuli/"+str(p)+"/"):
        print(link)
        try:
            urllib.request.urlretrieve(link,saveFile(link))
        except:
            print('失败')
