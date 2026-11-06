import my_module
words = ["Math","Art","Physics"]
index = my_module.find_word(words,"Math")
print(index)

# Other invoke
from my_module import  find_word
index = find_word(words,"Art")
print(index)