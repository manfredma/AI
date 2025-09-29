import re


class SimpleTokenizerV1:

    def __init__(self, vocab):
        # 将词汇表作为属性存储，以便在 encode 和 decode 方法中使用
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids ])
        # 去除特殊符号前的空格
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
