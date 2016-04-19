from pandas import *
import numpy as np
import re
from string import *
import sentlex
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

candidates = ['clinton','cruz','sanders','trump']
dates = [18,19,20,21,22,23,24,25,26,27,28,29]

# candidates = ['clinton']
# dates = [18]

SWN = sentlex.SWN3Lexicon()
classifier = sentlex.sentanalysis.BasicDocSentiScore()

def link_remove(message):
    x=re.sub("(https://[^ ]+)", "", message)
    return x

def at_removal(message):
    x = re.sub(r'(\s)@\w+', r'\1', message)
    return x

def positiveness_calc(message):
    x = message.encode('utf-8')
    x = at_removal(link_remove(x)).decode('utf-8')
    p, n = classifier.classify_document(x, tagged=False, L=SWN, a=True, v=True, n=False, r=False,negation=False, verbose=False)
    return p

def negativeness_calc(message):
    x = message.encode('utf-8')
    x = at_removal(link_remove(x)).decode('utf-8')
    p, n = classifier.classify_document(x, tagged=False, L=SWN, a=True, v=True, n=False, r=False,negation=False, verbose=False)
    return n

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

def pos_adj_calc(message):
    positive_adj = []
    for words in message.split():
        x,y = SWN.getadjective(words)
        positive_adj.append(x)
    return sum(positive_adj)

def neg_adj_calc(message):
    negative_adj = []
    for words in message.split():
        x,y = SWN.getadjective(words)
        negative_adj.append(y)
    return sum(negative_adj)


for item_candidates in candidates:
    for item_dates in dates:
        df = read_csv(open(item_candidates+'/count/'+item_candidates+'_03_'+str(item_dates)+'_count.csv', 'rU'), encoding='utf-8', engine='c')
        df1 = df[df['userLocation'].notnull()]
        print list(df1)
        df2 = pandas.DataFrame(columns=['tweetID', 'tweetText', 'tweetRetweetCt', 'tweetFavoriteCt', 'tweetSource', 'tweetCreated', 'userID',
                                'userScreen', 'userName', 'userCreateDt', 'userDesc', 'userFollowerCt', 'userFriendsCt', 'userLocation', 'userTimezone'])

        df1['positiveness'] = df1.tweetText.apply(positiveness_calc)
        df1['negativeness'] = df1.tweetText.apply(negativeness_calc)
        df1['sentiment_label'] = df1.tweetText.apply(senti_label)
        df1['pos_adj'] = df1.tweetText.apply(pos_adj_calc)
        df1['neg_adj'] = df1.tweetText.apply(neg_adj_calc)

        df1 = df1.drop('Unnamed: 0', 1)
        df1 = df1.drop('Unnamed: 0.1', 1)
        df1.to_csv(item_candidates+'/sentiment/'+item_candidates+'_03_'+str(item_dates)+'_sentiment.csv', sep=',', encoding='utf-8')





####################  UNIT TEST    ##############################################################
# print link_remove('The only Clinton I will vote for in 2016 https://t.co/oNx3rXbamp')

# print re.sub("(https:[^ ]+)", "","RT @freedomforusnow: Kasich would like voters to forget! Letter from Clinton thanking Kasich for his support of assault weapons ban.")

# print re.findall(r'\b@\w+',"Here is the machine that @realDonaldTrump will soon be fighting")
#
# print re.sub(r'(\s)@\w+', r'\1', 'Hello all please help @me   but#notme')
# print codec_change("RT @freedomforusnow: Kasich would like voters to forget! Letter from Clinton thanking Kasich for his support of assault weapons ban")

# print at_removal(link_remove('RT @TariqSmithNC: For comparison: The @Clinton campaign has over 2.5 million more votes.  https://t.co/E65RcB05C4'))

# print senti_label(at_removal(link_remove('RT @TariqSmithNC: For comparison: The @Clinton campaign has over 2.5 million more votes.  https://t.co/E65RcB05C4')))