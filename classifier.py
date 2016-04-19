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


def read_tweets(file, clas):
  print 'reading data form file'
  print file
  f = codecs.open(file, 'r',"utf-8")
  words = []
  line = f.readline()
  while line!='':
    words.append((tokenize_sentence(line),clas))
    line = f.readline()
  print "reading from file completed"
  return words

def tokenize_sentence(line):
    words1 = []
    stop = stopwords.words('english')
    stemmer = PorterStemmer()
    tokenizer = RegexpTokenizer('\w+')
    for word in tokenizer.tokenize(line):
        if word not in stop:
            x=stemmer.stem(word).encode('utf-8',errors='strict')
            words1.append(x)
    return words1

def classify(input):
  return classifier.classify(tokenize_sentence(input))

def train():
  positive_tweets = read_tweets('positive.txt', 'positive')
  negative_tweets = read_tweets('negative.txt', 'negative')
  print len(positive_tweets)
  print len(negative_tweets)

  pos_train = positive_tweets[:len(positive_tweets)]
  neg_train = negative_tweets[:len(negative_tweets)]
  # pos_test = positive_tweets[len(positive_tweets)*80/100+1:]
  # neg_test = negative_tweets[len(positive_tweets)*80/100+1:]

  training_data = pos_train + neg_train
  # test_data = pos_test + neg_test

  sentim_analyzer = SentimentAnalyzer()
  all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_data])
  unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
  print len(unigram_feats)

  sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
  training_set = sentim_analyzer.apply_features(training_data)

  # test_set = sentim_analyzer.apply_features(test_data)
  # print test_set

  trainer = NaiveBayesClassifier.train
  sentim_analyzer.train(trainer, training_set)

  # for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
  #   print('{0}: {1}'.format(key, value))
  # print sentim_analyzer.classify(tokenize_sentence('I hate driving car at night'))

  return sentim_analyzer


classifier = train()

f = open('bayes_full.pickle', 'wb')
pickle.dump(classifier, f)
f.close()