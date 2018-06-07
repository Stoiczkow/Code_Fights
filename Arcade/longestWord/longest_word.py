import string

def longestWord(text):
    result = ''
    print(string.punctuation)
    for punct in string.punctuation:
        text = text.replace(punct, ' ')
        
    splitted_text = text.split(' ')
    
    for word in splitted_text:
        if len(word) > len(result):
            result = word
            
    return result
