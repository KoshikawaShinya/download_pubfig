with open('dev_urls.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        data = line.split('\t')
        if i == 1000:
            break
        if len(data) != 5:
            continue
        else:
            name, num, url, rect, md5sum = data
            print(url[-4:])