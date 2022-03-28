urlDict = {}
url_taobao = "https://login.taobao.com/member/login.jhtml?spm=0.1.754894437.1.7483523cE8Xcus&f=top&redirectURL=https%3A%2F%2Fs.taobao.com%2F"
urlDict['taobao'] = url_taobao

url_kryst4l = "https://www.huya.com/222523"
urlDict['kryst4l'] = url_kryst4l

for i, key in enumerate(urlDict.keys()):
    print(f"{i:<5}{key:<10}")

index = int(input("输入想要获取的url的索引\n"))
key = list(urlDict.keys())[index]
url = urlDict[key]
print(url)

