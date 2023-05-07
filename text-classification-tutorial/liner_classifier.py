import pickle
import time
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
import os
from sklearn.linear_model import LogisticRegression

from training import X_train, y_train,X_test,y_test
import matplotlib.pyplot as plt


MODEL_PATH = "models"

if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
# train with Linear Classifier

start_time = time.time()
text_clf = Pipeline([
                    # Chuyển đổi văn bản thành vector đặc trưng bằng CountVectorizer của sklearn.
                    ('vect', CountVectorizer(ngram_range=(1, 1),
                                              max_df=0.8,
                                              max_features=None)),
                    # Tính toán trọng số IDF của các từ trong tài liệu bằng TfidfTransformer của sklearn.
                    ('tfidf', TfidfTransformer()),
                    # Huấn luyện mô hình phân loại tuyến tính trên các vector đặc trưng
                    # đã được tính toán bằng LogisticRegression của sklearn.
                    ('clf', LogisticRegression(solver='saga',
                                                multi_class='auto',
                                                max_iter=10000))
                    ])
text_clf = text_clf.fit(X_train, y_train)
accuracy = text_clf.score(X_test, y_test)
print("Accuracy:", accuracy)

train_time = time.time() - start_time
print('Done training Linear Classifier in', train_time, 'seconds.')
# Save model
pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "linear_classifier.pkl"), 'wb'))