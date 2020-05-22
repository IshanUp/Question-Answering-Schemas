from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'stanford-english-corenlp-2018-10-05-models')

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print 'Tokenize:', nlp.word_tokenize(sentence)
print 'Part of Speech:', nlp.pos_tag(sentence)
print 'Named Entities:', nlp.ner(sentence)
print 'Constituency Parsing:', nlp.parse(sentence)
print 'Dependency Parsing:', nlp.dependency_parse(sentence)

# Do not forget to close! The backend server will consume a lot memery.
nlp.close()
