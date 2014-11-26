#!/usr/bin/python2

import numpy, nltk, pprint, re  	
import os

def ie_preprocess(document):
   sentences = nltk.sent_tokenize(document)
   sentences = [nltk.word_tokenize(sent) for sent in sentences]
   sentences = [nltk.pos_tag(sent) for sent in sentences]
   return sentences

def np_chunk(sentence):
   processed_sentence = ie_preprocess(sentence)[0]
   grammar = r"""
  NP: 
     {<DT|PP\$>?<JJ>*<NN>*}   # chunk determiner/possessive, adjectives and noun
     {<NNS>}
  Subject: 
     {<NNP>+}      # sequences of proper nouns
     {<PRP|PRP\$>} # a personal pronoun or posessive pronoun
  VP: 
     {<VB|VB.>}
  rule1: 
     {<Subject><VP><NP>} # I am a powerlifter
  rule2: 
     {<Subject><VP>?<JJR><IN>?<Subject>} # I am stronger than James
  rule3: 
     {<Subject><NP|MD>?<VP><CD>} # I can benchpress 100, My benchpress max is 100, I benchpress 100 
  rule4: 
     {<Subject><VP><IN><NP>} # I lift in the morning
"""

   cp = nltk.RegexpParser(grammar)
   result = cp.parse(processed_sentence)
   return result

def convert_subject(phrase, client_name):

   pos = phrase[0][1]
   subtree = phrase
   noun = ""

   if pos == 'PRP' or pos == 'PRP$':
      return client_name
   else:
      for leaf in subtree:
         noun = noun + " " + leaf[0]

      return "'%s'" % noun.lower().strip()

def convert_np(phrase):

   np = None

   for leaf in phrase:
      if leaf[1] == "NN":
         if np == None:
            np = leaf[0]
         else:
            np = np + "_" + leaf[0]

   return "%s" % np.lower().strip()

def extract_meaning(sentence, client_name):
   tree = np_chunk(sentence)

   labels = ['rule1', 'rule2', 'rule3', 'rule4']
   trees = [x for x in tree if x.label() in labels]

   for tree in trees:
      name = tree.label()
      if name == labels[0]:   # rule1
         subject = convert_subject(tree[0], client_name)
         noun = tree[2][1][0]
         solution = "%s(%s)" % (noun, subject)
         return solution
      elif name == labels[1]: # rule2
         s1 = convert_subject(tree[0], client_name)
         s2 = convert_subject(tree[-1], client_name)
         comparison = [x[0] for x in tree if len(x) > 1 and x[1] == "JJR"]
         comparison = comparison[0]
         return "%s(%s, %s)" % (comparison, s1, s2)
      elif name == labels[2]: # rule3
         subject = convert_subject(tree[0], client_name)
         subtrees = tree.subtrees()

         nounPhrase = [x for x in subtrees if x.label() == "NP"]
         if len(nounPhrase) > 0:
            nounPhrase = convert_np(nounPhrase[0])
         else:
            nounPhrase = None

         subtrees = tree.subtrees()
         verbPhrase = [x for x in subtrees if x.label() == "VP"]         
         if len(verbPhrase) > 0:
            verbPhrase = verbPhrase[0][0][0]
         else:
            verbPhrase = None
 
         amount = tree[-1][0]
         predicate = verbPhrase
         if nounPhrase:
            predicate = nounPhrase
       
         return "%s(%s, %s)" % (predicate, subject, amount)  
      else:                   # rule4
         subject = convert_subject(tree[0], client_name)
         
         subtrees = tree.subtrees()
         nounPhrase = [x for x in subtrees if x.label() == "NP"]
         if len(nounPhrase) > 0:
            nounPhrase = convert_np(nounPhrase[0])
         else:
            nounPhrase = None

         subtrees = tree.subtrees()
         verbPhrase = [x for x in subtrees if x.label() == "VP"]         
         if len(verbPhrase) > 0:
            verbPhrase = verbPhrase[0][0][0]
         else:
            verbPhrase = None

         return "%s(%s, %s)" % (verbPhrase, subject, nounPhrase)
