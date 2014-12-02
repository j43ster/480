#!/usr/bin/python2

import numpy, nltk, pprint, re  	
import os
import nltk.tag, nltk.data

TELL = "tell"
ASK = "ask"

default_tagger = nltk.data.load(nltk.tag._POS_TAGGER)
model = {
   'stronger': 'JJR',
   'lift': 'VB',
   'am': 'VB',
   'Am': 'VB',
   '?': 'Question',
   'What': 'Question',
   'what': 'Question',
   '.': 'Tell',
   'powerlifter': 'NN',
}
tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)

def ie_preprocess(document):

   sentences = nltk.sent_tokenize(document)
   sentences = [nltk.word_tokenize(sent) for sent in sentences]
   sentences = [tagger.tag(sent) for sent in sentences]

   return sentences

def np_chunk(sentence):
   processed_sentence = ie_preprocess(sentence)[0]
   grammar = r"""
  Ignored:
     {<WP>|<MD>|<TO>|<RB|RB.>|<WRB>}
  IN:
     {<IN>}
  NP: 
     {<DT|PP\$>?<JJ>*<NN>*} # chunk determiner/possessive, adjectives and noun
     {<NNS>}
  Adjective:
     {<JJ>}
  Subject: 
     {<NNP>+<POS>?}      # sequences of proper nouns
     {<PRP|PRP\$>} # a personal pronoun or posessive pronoun
  Question:
     {<Question>}
  Tell:
     {<Tell>}
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

  rule1q: 
     {<VP><Subject><NP>} # Is Jeff a powerlifter? Am I a powerlifter?
  rule2q: 
     {<rule2><Question>} # Am I stronger than James, Is Jeff stronger than James
  rule3q: 
     {<WRB><VP><Subject><VP>} # When do I lift?, When does Jeff list?
  rule4q: 
     {<rule4><Question>} # Does Jeff lift in the morning?
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
      if not(leaf[1] == "DT"):
         if np == None:
            np = leaf[0]
         else:
            np = np + "_" + leaf[0]

   return "%s" % np.lower().strip()

def handle_rule1(tree, client_name):
   subject = convert_subject(tree[0], client_name)
   noun = convert_np(tree[2])
   solution = "%s(%s)" % (noun, subject)
   return (TELL, solution)

def handle_rule2(tree, client_name):
   s1 = convert_subject(tree[0], client_name)
   s2 = convert_subject(tree[-1], client_name)
   comparison = [x[0] for x in tree if len(x) > 1 and x[1] == "JJR"]
   comparison = comparison[0]
   return (TELL, "%s(%s, %s)" % (comparison, s1, s2))

def handle_rule3(tree, client_name):
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

   return (TELL, "%s(%s, %s)" % (predicate, subject, amount))  

def handle_rule4(tree, client_name):
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

   return (TELL, "%s(%s, %s)" % (verbPhrase, subject, nounPhrase))

def handle_rule1q(tree, client_name):
   subject = convert_subject(tree[1], client_name)
   noun = convert_np(tree[2])
   solution = "%s(%s)" % (noun, subject)
   return (ASK, solution)

# {<rule2><Question>} # Am I stronger than James, Is Jeff stronger than James
def handle_rule2q(tree, client_name):
   (tell, meaning) = handle_rule2(tree[0], client_name)
   return (ASK, meaning)

# {<WRB><VP><Subject><VP>} # When do I lift?, When does Jeff list?
def handle_rule3q(tree, client_name):
   subject = convert_subject(tree[2], client_name)

   predicate = [x for x in tree.subtrees() if x.label() == "VP"]         
   if len(predicate) > 1:
      predicate = predicate[1][0][0]
   else:
      predicate = None

   return (ASK, "%s(%s, X)" % (predicate, subject))

# {<rule4><Question>} # Am I stronger than James, Is Jeff stronger than James
def handle_rule4q(tree, client_name):
   (tell, meaning) = handle_rule4(tree[0], client_name)
   return (ASK, meaning)

def extract_meaning(sentence, client_name):
   tree = np_chunk(sentence)

   labels = ['rule1', 'rule2', 'rule3', 'rule4', 'rule1q', 'rule2q', 'rule3q', 'rule4q']
   trees = [x for x in tree if x.label() in labels]

   for tree in trees:
      name = tree.label()
      if name == labels[0]:   # rule1
         return handle_rule1(tree, client_name)
      elif name == labels[1]: # rule2
         return handle_rule2(tree, client_name)
      elif name == labels[2]: # rule3
         return handle_rule3(tree, client_name)
      elif name == labels[3]: # rule4
         return handle_rule4(tree, client_name)
      elif name == labels[4]: # rule1q
         return handle_rule1q(tree, client_name)
      elif name == labels[5]: # rule2q
         return handle_rule2q(tree, client_name)
      elif name == labels[6]: # rule2q
         return handle_rule3q(tree, client_name)
      elif name == labels[7]: # rule4q
         return handle_rule4q(tree, client_name)
      else:
         pass

   return (None, None)
