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
        if os.path.exists('bystate_results/'+item_states+'/'+item_candidates+'.csv'):
            df = read_csv(open('bystate_results/'+item_states+'/'+item_candidates+'.csv', 'rU'), encoding='utf-8', engine='c')
            df1 = df[df['userLocation'].notnull()]
            print list(df1)
            df2 = pandas.DataFrame(columns=['tweetID', 'tweetText', 'positiveness','negativeness','pos_adj','neg_adj'])
            count_pos = 0
            count_neg = 0
            count_pos_adj = 0
            count_neg_adj = 0

            for index, row in df1.iterrows():
                x1 = row['positiveness']
                x1_wt = row['Weight']
                x1 = x1*x1_wt
                count_pos = count_pos + x1

            for index, row in df1.iterrows():
                x2 = row['negativeness']
                x2_wt = row['Weight']
                x2 = x2 * x2_wt
                count_neg = count_neg + x2

            for index, row in df1.iterrows():
                x3 = row['pos_adj']
                x3_wt = row['Weight']
                x3 = x3 * x3_wt
                count_pos_adj = count_pos_adj + x3

            for index, row in df1.iterrows():
                x4 = row['neg_adj']
                x4_wt = row['Weight']
                x4 = x4 * x4_wt
                count_neg_adj = count_neg_adj + x4

            my_file = open('bystate_results/'+item_states+'/'+item_candidates+'_results_weighted_2.txt', 'a')
            my_file.write('positiveness' + ': ' + str(count_pos) + '\n')
            my_file.write('negativeness' + ': ' + str(count_neg) + '\n')
            my_file.write('positiveness_adj' + ': ' + str(count_pos_adj) + '\n')
            my_file.write('negativeness_adj' + ': ' + str(count_neg_adj) + '\n')
            my_file.write('results' + ': ' + str((count_pos+count_pos_adj)-(count_neg+count_neg_adj)) + '\n')
            my_file.close()

