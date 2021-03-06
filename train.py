import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import sklearn.datasets as skd
from sklearn.externals import joblib

# define the categories
categories = ['invoice', 'bank', 'agreement']
news_train = skd.load_files('/home/codemantra/Documents/bhargh@va/learning/hackathon/intelligentDocuments/text/train/',
                            categories=categories, encoding='ISO-8859-1')
news_test = skd.load_files('/home/codemantra/Documents/bhargh@va/learning/hackathon/intelligentDocuments/text/test/',
                           categories=categories, encoding='ISO-8859-1')


text_clf = Pipeline([('vect', TfidfVectorizer()),
                     ('clf', MultinomialNB())])

# train the model
text_clf.fit(news_train.data, news_train.target)
# Predict the test cases
predicted = text_clf.predict(news_test.data)


print('Accuracy achieved is ' + str(np.mean(predicted == news_test.target)))
print(metrics.classification_report(news_test.target,
      predicted, target_names=news_test.target_names)),
metrics.confusion_matrix(news_test.target, predicted)
joblib.dump(text_clf, 'text_model.pk1')
