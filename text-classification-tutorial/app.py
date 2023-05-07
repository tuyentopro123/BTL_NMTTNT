from flask import Flask, jsonify, request
import pickle
import os
from flask_cors import CORS
from util import remove_stopwords
from main import text_preprocess
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
fileData = 'data_preprocessing\\news_categories.prep'
text = []
label = []

for line in open(fileData, encoding='utf-8'):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=0.2, random_state=42)

label_encoder = LabelEncoder()
label_encoder.fit(y_train)
MODEL_PATH = "models"
with open(os.path.join(MODEL_PATH, "linear_classifier.pkl"), 'rb') as model_file:
    nb_model = pickle.load(model_file)
stopword = set()
with open('news_categories\\stopwords.txt', 'r',encoding='utf-8') as fp:
    for word in fp:
        word = word.strip()
        stopword.add(word)

# thông tin dữ liệu
count1 = {}
count2 = {}
for line in y_train:
    key = line
    count1[key] = count1.get(key, 0) + 1
for line in y_test:
    key = line
    count2[key] = count2.get(key, 0) + 1
total_count = sum(count1.values())
total_count2 = sum(count2.values())

label_train_percentages = []
label_test_percentages = []
for key in count1:
    percentage = (count1[key] / total_count) * 100
    label_train_percentages.append({
        "name": " ".join(key.replace("__label__","").split("_")),
        "percent": round(percentage, 2),
        "quantity": count1[key]
    })

for key in count2:
    percentage = (count2[key] / total_count2) * 100
    label_test_percentages.append({
        "name": " ".join(key.replace("__label__","").split("_")),
        "percent": round(percentage, 2),
        "quantity": count2[key]
    })
# APP
app = Flask(__name__)
CORS(app)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    document = data['document']
    if document != '':
        document = text_preprocess(document)
        document = remove_stopwords(document, stopword)
        label = nb_model.predict([document])
        response = jsonify({
            'label':label_encoder.inverse_transform(label)[0].replace("__label__",""),
            'err': 'false'
        })
    else :
        response = jsonify({
            'label': 'Bạn cần nhập gì đó để dự đoán',
            'err': 'true'
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/data', methods=['GET'])
def data():
    response = jsonify({'data1': label_train_percentages,'data2':label_test_percentages})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    app.run(debug=True)