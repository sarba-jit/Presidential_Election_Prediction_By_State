import nltk
from codecs import *
from nltk.tokenize import RegexpTokenizer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.stem.porter import *
import codecs
import pickle

#
# f= open('bayes_half.pickle')
# classifier = pickle.load(f)
# f.close()

def link_remove(message):
    x=re.sub("(https://[^ ]+)", "", message)
    return x

def at_removal(message):
    x = re.sub(r'(\s)@\w+', r'\1', message)
    print x
    return x

def tokenize_sentence(line):
    words1 = []
    stop = stopwords.words('english')
    stemmer = PorterStemmer()
    tokenizer = RegexpTokenizer('\w+')
    for word in tokenizer.tokenize(line):
        if word not in stop:
            # try:
            x=stemmer.stem(word).encode('utf-8',errors='strict')
            words1.append(x)
    return words1

def senti_label(message):
    f = open('bayes_half.pickle')
    classifier = pickle.load(f)
    f.close()
    label = classifier.classify(tokenize_sentence(message))
    return label


message = 'Here is the machine that @realDonaldTrump will soon be fighting. https://t.co/oEzyNwm1Ie #bad #Trump2016 https://t.co/1wembRJIrN'
print senti_label(at_removal(link_remove(message)))