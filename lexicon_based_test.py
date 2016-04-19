import sentlex
# import sentlex.sentanalysis
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

SWN = sentlex.SWN3Lexicon()
# SWN = sentlex.UICLexicon()
# SWN = sentlex.MobyLexicon()

classifier = sentlex.sentanalysis.BasicDocSentiScore()
# classifier = sentlex.DocSentiScore()
print SWN.hasadjective('bad')
# print SWN.getverb('muslim')

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


def read_tweets(file):
  print 'reading data form file'
  print file
  f = codecs.open(file, 'r',"utf-8")
  line = f.readline()
  line_count =[]
  # print line
  while line!='':
      line_count.append(line)
      line = f.readline()


  print "reading from file completed"
  # print line_count[8]
  return line_count

def summation(list):
    count = 0
    for item in list:
        count = count +item
    return count


def link_remove(message):
    x=re.sub("(https://[^ ]+)", "", message)
    return x

def at_removal(message):
    x = re.sub(r'(\s)@\w+', r'\1', message)
    print x
    return x
# positive_tweets = read_tweets('positive2.txt')
# negative_tweets = read_tweets('negative2.txt')
def adj_sentiment_score(item):
    # for item in negative_tweets:
    print item
    positive_adj = []
    negative_adj = []
    for words in item.split():
        x,y = SWN.getadjective(words)
        positive_adj.append(x)
        negative_adj.append(y)

        print words+ ': '+ str(x) + ' and '+str(y)
    print sum(positive_adj)
    print sum(negative_adj)


# adj_sentiment_score("Here is the machine that @realDonaldTrump will soon be fighting. https://t.co/oEzyNwm1Ie #bad #Trump2016 https://t.co/1wembRJIrN")

    # print classifier.classify_document(item, tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=False, verbose=False)

print classifier.classify_document('obama better win, or else im going to live and be happy in another country.', tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=False, verbose=False)

