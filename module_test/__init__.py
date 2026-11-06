import my_module
from sys import path
import os

words = ["Math","Art","Physics"]
index = my_module.find_word(words,"Math")
print(index)

# Other invoke
from my_module import  find_word
index = find_word(words,"Art")
print(index)

print(path)
print(os.getcwd())
# path.append(os.getcwd())