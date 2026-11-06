print("this is my module")

def find_word(words,target):
    for  index,word in enumerate(words):
        if word == target:
            return index
    return -1
