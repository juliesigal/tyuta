# tyuta**

פונקציה שמקבלת מילה ומחזירה אותה חבויה:
 
 
def convert_word(_word = 'trust'):
    new_word = _word
    print(new_word)
    for i in _word:
        print(i)
        new_word = new_word.replace(i,'_')
        print(new_word)
    return new_word
