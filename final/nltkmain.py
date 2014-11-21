#!/usr/bin/python2

import parser as p
import nltk, re

keywords = ["name", "max", "maximum", "bench", "press"]

print("Hi, I am a chat bot with some weight lifting knowledge.")

name = raw_input('What is your name? ')

print(name)

name_sentence = p.np_chunk(name)
print(name_sentence)

while(True):
   raw_sentence = raw_input('Do you have anything else to say? ')

   if (raw_sentence == "no"):
      break

   # pull out NN here and see if any are in keywords
   # if they are, try to get info from the sentence

   sentence_chunk = p.np_chunk(raw_sentence)
   print("sentence_chunk: " + str(sentence_chunk))
   p.extract_relations([sentence_chunk])
   sentence_chunk.draw()

#IN = re.compile(r'.*\bin\b(?!\b.+ing)')
#for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
#   print(doc)
#   for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
#      print(nltk.sem.rtuple(rel))

#print(nltk.corpus.ieer)
