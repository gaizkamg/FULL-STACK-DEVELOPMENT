#Find method returns the index of the start of the word
#Search the word "quick"

sentence= "The quick brown fox jumped quickly!"
query= sentence.find('quick')

#We can search within a range
query2= sentence.find("quick",9,25)

print('query1: ' + str(query) )
print('query2: ' + str(query2) )

#If find method doesn't find the substring it returns -1
query3= sentence.find('sky')

print('query3: ' + str(query3) )

#Index method is the same but 
query4= sentence.index('fox')
print('query4: ' + str(query4) )

#it will drop an error if can't find it
query5= sentence.index('@')
print('query5: ' + str(query5) )