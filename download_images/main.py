import urllib.request
from datetime import datetime


def download_img(url):
    time = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_path = './download_images/img/' + time + '.jpg'
    urllib.request.urlretrieve(url, full_path)


url = input('Enter a image url: ')

download_img(url)
