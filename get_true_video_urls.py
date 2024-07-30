import requests
import re
def get_url_and_name(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    before = re.findall('''                                     <li ><a href="(.*?)">(.*?)</a></li>''',response.text)
    url_list = []
    name = []
    for i in before:
        if "1-" in i[0]:
            url_list.append(i[0])
            name.append(i[1])
    return name, url_list
def get_video_url(url):
    new_url = "https://www.libvio.fun" + url
    response = requests.get(new_url)
    response.encoding = response.apparent_encoding
    video_url_parameter = re.findall('''"url":"(.*?)",''',response.text)[0]
    next_url = re.findall('''"link_next":"(.*?)"''',response.text)[0]
    next_url = next_url.replace('\\','')
    video_url = "https://www.libvio.fun/vid/plyr/?url=%s&next=%s&id=4632&nid=1" % (video_url_parameter,next_url)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'referer' : new_url
    }
    video_response = requests.get(video_url,headers=headers)
    the_last_video_url = re.findall("var urls = '(.*?)';",video_response.text)[0]
    return the_last_video_url
    # print(video_response.text)
def get_urls(video_url):
    name,url_list = get_url_and_name(video_url)
    video_urls = []
    for url in url_list:
        video_urls.append(get_video_url(url))
    return name,video_urls