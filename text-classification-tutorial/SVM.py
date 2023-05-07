from sklearn.svm import SVC
import pickle
import time
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
import os

from training import X_train, y_train,X_test,y_test

MODEL_PATH = "models"

if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
start_time = time.time()
text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
                                             max_df=0.8,
                                             max_features=None)),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SVC(gamma='scale'))
                    ])
text_clf = text_clf.fit(X_train, y_train)
accuracy = text_clf.score(X_test, y_test)
print("Accuracy:", accuracy)

train_time = time.time() - start_time
print('Done training SVM in', train_time, 'seconds.')

# Save model
pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "svm.pkl"), 'wb'))