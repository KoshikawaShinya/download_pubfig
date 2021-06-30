import os
import urllib
from urllib import request
import requests


with open('dev_urls.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 1500:
            continue
        data = line.split('\t')
        if len(data) != 5:
            continue
        else:
            name, num, url, rect, md5sum = data
            print(name, num, url)
        if not os.path.exists('images/{}'.format(name)):
            os.mkdir('images/{}'.format(name))
        try:
            est = url[-4:]
            file_name= 'images/{}/{}{}'
            response = requests.get(url, timeout=(3.0, 5.0), allow_redirects=False)
            image = response.content
            with open(file_name.format(name, num, est), 'wb') as im:
                im.write(image)
            #request.urlretrieve(url, 'images/{}/{}.jpg'.format(name, num))
        except requests.exceptions.ConnectionError:
            print('Error occured')
        except requests.exceptions.Timeout:
            print('Timeout')
    
    