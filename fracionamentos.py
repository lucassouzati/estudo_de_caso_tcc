#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json
from nltk import tokenize
# import nltk
from collections import defaultdict

def map_reduce(inputs):
	collector = defaultdict(list)
	# print(inputs)
	for input in inputs:
		for key, value in mapper(input):
			collector[key].append(value)

	return [output
			for key, values in collector.iteritems()
			for output in reducer(key,values)]

def mapper(document):
	for word in document.split(' '):
		print(word)
		yield (word, 1)

def reducer(word, counts):
	# print(word)
	yield (word, sum(counts))

endpoint = "http://slacs.dev/api/contratos/itens"
saida = json.loads(requests.get(endpoint).text)
# print saida[0]['descricao']
valores = set()
for item in saida:
	valores.add(item['descricao'])
	
print(sorted(map_reduce(valores),
	key=lambda (word, count): count,
	reverse=True))

