sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)

string = "I'm the inmutable string"
print(string)
print('ID:',id(string))
string += " with new friends"
print(string)
print('ID:',id(string))#As we can see here, in the memory is stored a string with an ID and after reasigning with more elements python has created another tuple with the same name