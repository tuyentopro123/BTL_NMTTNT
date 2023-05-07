from tqdm import tqdm
from util import remove_stopwords

count = {}
fileCategory = 'news_categories\\news_categories.txt'
print("Thống kê số lượng nhãn theo data:")
with open(fileCategory, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]
for line in tqdm(lines):
    key = line.split()[0]
    count[key] = count.get(key, 0) + 1

print("Số lượng nhãn theo data:")
for key in count:
    print("+",key.replace("__label__",""),":", count[key])


# Thống kê các word xuất hiện ở tất cả các nhãn
total_label = 18
vocab = {}
label_vocab = {}
print("Thống kê số lượng từ stopword:")
for line in tqdm(lines):
    words = line.split()
    # lưu ý từ đầu tiên là nhãn
    label = words[0]
    if label not in label_vocab:
        label_vocab[label] = {}
    for word in words[1:]:
        label_vocab[label][word] = label_vocab[label].get(word, 0) + 1
        if word not in vocab:
            vocab[word] = set()
        vocab[word].add(label)

count = {}
for word in vocab:
    if len(vocab[word]) == total_label:
        count[word] = min([label_vocab[x][word] for x in label_vocab])

sorted_count = sorted(count, key=count.get, reverse=True)

print("Lấy ra 10 từ đầu tiên: ")
for word in sorted_count[:10]:
    print(word,":",count[word])

stopword = set()
with open('news_categories\\stopwords.txt', 'w',encoding='utf-8') as fp:
    for word in sorted_count[:100]:
        stopword.add(word)
        fp.write(word + '\n')

# loại stopword khỏi dữ liệu và lưu file
fileData = 'data_preprocessing\\news_categories.prep'
with open(fileData, 'w',encoding='utf-8') as fp:
    for line in open(fileCategory,encoding='utf-8'):
        line = remove_stopwords(line,stopword)
        fp.write(line + '\n')