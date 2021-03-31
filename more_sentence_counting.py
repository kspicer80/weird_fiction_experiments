import spacy
nlp = spacy.load('en_core_web_lg')

rb_tc = open('rb_tc.txt').read()
text = nlp(rb_tc)
cleaned_text = [token for token in text if not token.is_punct]

print(len(text))
print(cleaned_text)

sentenceLengths = [len(sent) for sent in text_sents]
print(text_sents[0])
print(sentenceLengths[0])

sample_sentence = nlp("Mr. Spallner put his hands over his face.")

print('''
words\t\t{num_words}
sentences\t{num_sent}
'''.format(
    num_words=len(sample_sentence),
    num_sent=len(list(sample_sentence.sents))
))

cleaned = [token for token in sample_sentence if not token.is_punct]
for token in cleaned:
    print(token.text)
print(len(cleaned))
