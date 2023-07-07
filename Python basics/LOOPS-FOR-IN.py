fruits = ['Strawberry','Banana','Apple'] #we have a list with 3 elements inside

for i in fruits: # we are giving an interation variable in the for that could be anything, i, x, fruit, z. Is good to be a name that represent the element
    print(i)


players = { #now we have a dictionary with 4 key/value elements
    'player1' : 'Gaizka',
    'player2' : 'Edu',
    'player3' : 'Sandra',
    'player4' : 'Helen',
}

for player, name in players.items(): #we must use another approach with dictionaries so we are calling a function: items().
    print('Player#', player)
    print('Name', name)


for num in range(10): #if we don't specify the beggining starts from 0 and stops just before the 10, in other words 9
    print(num)

for num in range(4,10): #if we specify the beggining starts from 4 and stops just before the 10.
    print(num)


usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]
#when we use continue the loop will continue and the code will be generated
for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

#when we use break the loop will stop and the print(username) will not be executed
for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)


def loop_and_break():
    vegetables = ["onion", "broccoli", "apple", "spinach"]
    
    for veg in vegetables:
        if veg == 'apple':
            print(f'{veg} is not a vegetable')
            break
print(loop_and_break())
    