# from underthesea import word_tokenize
# sentence = 'Chú bé đần và Chàng trai Nam Định chạy Ahamovel'
#
# print(word_tokenize(sentence, format="text"))
# Thống kê các word xuất hiện ở tất cả các nhãn
total_label = 18
vocab = {}
label_vocab = {}
for line in open('news_categories/news_categories.txt'):
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
for word in sorted_count[:100]:
    print(word, count[word])