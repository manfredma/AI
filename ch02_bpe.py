from importlib.metadata import version

import tiktoken

print('tiktoken version', version('tiktoken'))

tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)

strings = tokenizer.decode(integers)
print(strings)

integers = tokenizer.encode("Akwirw ier")
print(integers)
for integer in integers:
    print(tokenizer.decode([integer]))