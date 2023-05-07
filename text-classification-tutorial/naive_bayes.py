import pickle
import time
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from training import X_train, y_train,X_test,y_test
MODEL_PATH = "models"

if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
start_time = time.time()

text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
                                             max_df=0.8,
                                             max_features=None)), 
                     ('tfidf', TfidfTransformer()), 
                     ('clf', MultinomialNB())
                    ])
text_clf = text_clf.fit(X_train, y_train)
accuracy = text_clf.score(X_test, y_test)
print("Accuracy:", accuracy)

train_time = time.time() - start_time
print('Done training Naive Bayes in', train_time, 'seconds.')

# Save model
pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "naive_bayes.pkl"), 'wb'))