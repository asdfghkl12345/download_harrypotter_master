import download
import os
import get_true_video_urls
name,video_url = get_true_video_urls.get_urls("https://www.libvio.fun/detail/4632.html")
# print(name,video_url)
for i in range(len(video_url)):
    data_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'download')
    print("正在下载：哈利波特与" + name[i])
    downloader = download.DownloadFile(video_url[i],data_folder,50,'哈利波特与' + name[i]+'.mp4')
    downloader.main()