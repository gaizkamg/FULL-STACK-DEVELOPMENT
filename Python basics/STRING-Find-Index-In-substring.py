sentence = 'The quick brown fox jumped over the lazy dog.'
query = sentence.find('quick')
print(query) #give us the index of the element we have searched >> 4


query = sentence.find('oops') #this will return -1 if the word is not found
query_two = sentence.index('brown')

print(query)
print(query_two)


query = 'lazy' in sentence #this will return True if the word is found
print(query)


query = 'oops' in sentence #this will return False if the word is not found
print(query)