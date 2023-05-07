import pickle
import os
from sklearn.preprocessing import LabelEncoder
from classify import fileData
from sklearn.model_selection import train_test_split
text = []
label = []

for line in open(fileData, encoding='utf-8'):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=0.2, random_state=42)
# from training import label_encoder
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
# Define LabelEncoder
# Load model
MODEL_PATH = "models"
linear_clf = pickle.load(open(os.path.join(MODEL_PATH, "linear_classifier.pkl"), 'rb'))
# Test model
from util import remove_stopwords
from main import text_preprocess

document = "Cách đây ba năm, Trường ĐH Kinh tế TP.HCM đưa ra chính sách khen thưởng cho giảng viên có bài báo công bố quốc tế. Mức thưởng cao nhất 200 triệu đồng/bài. Số lượng bài báo công bố quốc tế của trường cũng tăng dần đều trong những năm gần đây. Trong đó, năm 2016 có 44 bài, 2017 là 57 bài, 2018 là 60 bài và năm 2019 có 82 bài." \
           "GS.TS Nguyễn Trọng Hoài - phó hiệu trưởng Trường ĐH Kinh tế TP.HCM - cho biết chính sách khuyến khích cũng phần nào giúp gia tăng bài báo quốc tế của trường bên cạnh các quy định về nghiên cứu khoa học bắt buộc đối với giảng viên, số tiến sĩ tăng, thành lập các nhóm nghiên cứu mạnh. Kinh phí thưởng tối đa mỗi năm khoảng 2 tỉ đồng." \
           "Trong khi đó, số bài báo công bố quốc tế của Trường ĐH Mở TP.HCM tăng từ 16 bài năm 2017 lên 62 bài năm 2018. PGS.TS Nguyễn Minh Hà, hiệu trưởng nhà trường, cho biết trường bắt đầu chính sách thưởng công bố quốc tế từ năm 2017 và có điều chỉnh mức thưởng theo hướng tăng lên. Mức thưởng dao động từ 40-100 triệu đồng/bài tùy loại tạp chí."
stopword = set()
document = text_preprocess(document)
print(document)
with open('news_categories\\stopwords.txt', 'r', encoding='utf-8') as fp:
    for word in fp:
        word = word.strip()
        stopword.add(word)
document = remove_stopwords(document,stopword)
label = linear_clf.predict([document])
print('Predict label:', label_encoder.inverse_transform(label)[0])