from bs4 import BeautifulSoup
from tqdm import tqdm

while True:
    print("Меню:\n 1. Парсинг ссылок\n 2. Скачать видосик")
    x = input("Выберите пункт меню:\n")
    x = int(x)

    if x == 1:
        import requests

        url = "https://m2.semyana.biz"

        requests = requests.get(url)

        soup = BeautifulSoup(requests.text, "html.parser")

        title = soup.find_all("div", class_="b--video-medium__info")

        for titles in title:
            titles = titles.find("a", {'class':'b--video-medium__title'})

            if titles is not None:
                sublink = titles.get('href')
                print(str(titles.text) + "  " + "https://m2.semyana.biz" + str(sublink))
                print("===============")

    elif x == 2:
        import requests

        url = input("Введите ссылку: ")

        repka = requests.get(url)

        soup = BeautifulSoup(repka.text, "html.parser")

        vid = soup.find_all("div", class_="b--page-video__video-big")

        for vids in vid:
            vids = soup.find("source").get("src")

        chunk_size = 1024

        def download_video(url=''):
            try:
                response = requests.get(url=url, stream=True)
                total_size = int(response.headers['content-length'])
                
                with open ('req_video.mp4', 'wb') as file:
                    for video in tqdm(iterable = response.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit = 'KB'):
                        file.write(video)

                return 'Видео скачано!'
            except Exception as _ex:
                return 'Error!'

        print(download_video(url=vids))