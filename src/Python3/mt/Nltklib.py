import nltk
import jieba

def Get_FreqDist(keystr='',language_temp='en'):
	if language=='en':
		return nltk.FreqDist(nltk.WordPunctTokenizer().tokenize(keystr))
	if language=='zh':
		return nltk.FreqDist(list(jieba.cut(s)))