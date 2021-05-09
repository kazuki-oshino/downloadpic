# coding: utf-8

import urllib.request
import csv
import time

PATH = './downloadpic/main/{}.jpg'
CSV = './downloadpic/main/imgurl.csv'
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
START = 0


def download_image(url, title):
    print(url)
    request = urllib.request.Request(url=url, headers=HEADERS)
    with open(title, "wb") as f:
        f.write(urllib.request.urlopen(request).read())


def download():
    with open(CSV, newline='') as csv_file:
        count = START
        for row in csv.reader(csv_file):
            time.sleep(1)
            count += 1
            url = row[0]
            download_image(url, PATH.format(str(count)))


if __name__ == "__main__":
    print('ダウンロード開始')
    download()
    print('ダウンロード終了')
