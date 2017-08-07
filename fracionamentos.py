#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json
# from nltk import tokenize
import nltk
# from nltk.tokenize import RegexpTokenizer
from collections import defaultdict

def map_reduce(inputs):
	collector = defaultdict(list)

	for input in inputs:
		for key, value in mapper(input):
			collector[key].append(value)

	return [output
			for key, values in collector.iteritems()
			for output in reducer(key,values)]

def mapper(document):
	stopwords = nltk.corpus.stopwords.words('portuguese')
	punctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
	# toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
	for word in nltk.word_tokenize(document):
		if word not in stopwords and word not in punctuations:
			yield (word, 1)

def reducer(word, counts):
	yield (word, sum(counts))

endpoint = "http://slacs.dev/api/contratos"
saida = json.loads(requests.get(endpoint).text)
# print saida[0]['descricao']
valores = set()
for item in saida:
	print(item['descricao'])
	valores.add(item['descricao'])
	
print(sorted(map_reduce(valores),
	key=lambda (word, count): count,
	reverse=True))
# print(nltk.corpus.stopwords.words('portuguese'))
