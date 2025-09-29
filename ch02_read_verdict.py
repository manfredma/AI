import re

from ch02_simple_tokenizer_v1 import SimpleTokenizerV1

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of charactor: ", len(raw_text))
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
print("Total number of charactor after preprocessed: ", len(preprocessed))
print(preprocessed[:30])

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("Total number of words: ", vocab_size)

vocab = {token:integer for integer, token in enumerate(all_words)}
print("Vocabulary size: ", len(vocab))
for i, item in enumerate(vocab.items()):
    print(i, item)
    if i > 50:
        break


tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

print(tokenizer.decode(ids))