#!/usr/bin/python2

import numpy, nltk, pprint, re  	
import os

clear = lambda: os.system('clear')

def ie_preprocess(document):
   sentences = nltk.sent_tokenize(document)
   sentences = [nltk.word_tokenize(sent) for sent in sentences]
   sentences = [nltk.pos_tag(sent) for sent in sentences]
   return sentences

def np_chunk(sentence):
   processed_sentence = ie_preprocess(sentence)[0]
   print "ps: %s" % processed_sentence
   grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>*}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
"""
   cp = nltk.RegexpParser(grammar)
   result = cp.parse(processed_sentence)
   return result

def extract_relations(sentences):
   IN = re.compile(r'.*\bin\b(?!\b.+ing)')
   #for doc in nltk.corpus.ieer.parsed_docs(sentences):
#   for rel in nltk.sem.extract_rels('ORG', 'LOC', sentences, corpus='ieer', pattern = IN):
#      print(nltk.sem.rtuple(rel))

