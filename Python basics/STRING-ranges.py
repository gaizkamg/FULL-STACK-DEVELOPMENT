#Extract the word "pie" using Ranges. Remember in python indexes start at 0. The last number of range must be the next after the letter we are searching for, example: pie starts in the index 5 with "p" and ends in 7 with "e", but in order to get the whole word we must sum up a number to that range and end in the 8 index number. 
#S=0  o=1  m=2  e=3
sentence = "Some pie please!"
sub_sentence = sentence[5:8]
print('range 5-8: ', sub_sentence)