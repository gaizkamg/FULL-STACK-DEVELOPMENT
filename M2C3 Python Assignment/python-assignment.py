#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
sentence = 'The truth is that we are made of stardust'
number = 8
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'urane', 'neptune']
life = True

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
three_letters = sentence[0:3]
print('three_letters:', three_letters)

#Exercise 3: Use an index to grab the first element from your list.
first_planet = planets[0]
print('first planet: ', first_planet)

#Exercise 4: Create a new number variable that adds 10 to your original number.
new_number = number + 10
print('new_number: ', new_number)

#Exercise 5: Use an index to get the last element in your list.
last_planet = planets[-1]
print('last_planet: ', last_planet)

#Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print('names_list: ', names_list)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
first_word = sentence[0:4]
new_sentence = first_word.upper() + sentence[4:]
print('new sentence:', new_sentence)

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
fact_sentence = f"There are {number} planets on the solar system, because Pluto is no longer a planet but a dwarf planet"
print('fact sentence: ', fact_sentence)

#Exercise 9: Print “hello world”.
print("hello world")



