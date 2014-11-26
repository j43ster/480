#!/usr/bin/python2

import parser as p
import nltk, re

keywords = ["name", "max", "maximum", "bench", "press"]

while(True):
   raw_sentence = raw_input(':')

   if (raw_sentence == "no"):
      break

   # pull out NN here and see if any are in keywords
   # if they are, try to get info from the sentence

   sentence_chunk = p.ie_preprocess(raw_sentence)
   print("sentence_chunk: " + str(sentence_chunk))

#IN = re.compile(r'.*\bin\b(?!\b.+ing)')
#for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
#   print(doc)
#   for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
#      print(nltk.sem.rtuple(rel))

#print(nltk.corpus.ieer)
