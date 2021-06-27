
# 名前をラベルにするディクショナリ
name2label = {}
# [名前, 番号, url] の二次元配列にする
data_urls = []

with open('dev_people.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    for i, x in enumerate(data.splitlines()[2:]):
        name2label[x] = i

with open('dev_urls.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    
    for i, x in enumerate(data.splitlines()[2:]):
        data_urls.append([x for x in data.split('\t')])
print(data_urls)
    
