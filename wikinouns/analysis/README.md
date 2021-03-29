Some quick notes on features:

What do the columns mean?

The word classes from the nltk pos_tag function are described here:
https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/

CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent‘s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go ‘to‘ the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when


Here is an example column name:

freq_1ov2_nn_nns

The 1ov2 portion of the column name means that this feature corresponds to the first half of the body of text for the wikipedia article.
If the feature had 2ov2 instead, that would mean it corresponds to the second half of the body of text.
The nn_nns indicates that the feature is the frequency of nn class words followed by the nns class words. 
So in this case it is the proportion of word pairs that are nouns followed by plural nouns.


