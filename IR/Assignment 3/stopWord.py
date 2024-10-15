from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))
file1 = open("./input.txt")


line = file1.read()
words = line.split()
for r in words:
	if not r in stop_words:
		appendFile = open('output.txt','a')
		appendFile.write(" "+r)
		appendFile.close()