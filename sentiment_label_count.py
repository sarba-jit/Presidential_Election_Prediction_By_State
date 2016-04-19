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
import os.path

states = ['alaska','arizona','hawaii','idaho','northdakota','utah','washington','wisconsin','wyoming']
candidates = ['clinton','cruz','sanders','trump']

# states = ['alaska']
# candidates = ['clinton']

for item_states in states:
    for item_candidates in candidates:
        if os.path.exists('bystate_results_labelled/'+item_states+'/'+item_candidates+'.csv'):
            df = read_csv(open('bystate_results_labelled/'+item_states+'/'+item_candidates+'.csv', 'rU'), encoding='utf-8', engine='c')
            df1 = df[df['userLocation'].notnull()]
            print list(df1)
            df2 = pandas.DataFrame(columns=['tweetID', 'tweetText', 'positiveness','negativeness','pos_adj','neg_adj'])
            count_pos = 0
            count_neg = 0


            for index, row in df1.iterrows():
                x1 = row['sentiment_label']
                if (x1=='positive'):
                    count_pos = count_pos + 1

            for index, row in df1.iterrows():
                x1 = row['sentiment_label']
                if (x1=='negative'):
                    count_neg = count_neg + 1

            my_file = open('bystate_results_labelled/'+item_states+'/'+item_candidates+'_sentiment_label.txt', 'a')
            my_file.write('positiveness' + ': ' + str(count_pos) + '\n')
            my_file.write('negativeness' + ': ' + str(count_neg) + '\n')
            my_file.close()
