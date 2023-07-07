# Single condition
age = 25

if age < 25:
  print(f"I'm sorry, you need to be at least 25 years old")

# if/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

# if/elif/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is over 100 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

#Ternary operator>> write the if/else statement in one line
role = 'guest'
auth = 'can access' if role == 'admin' else 'cannot access'

#this is the same as the following conditional:
if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)




# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

username = 'jonsnow'

if username == 'jonsnow':
  print('Welcome Jon')
else:
  print('You shall not pass!')

age = 25

if age <= 25:
  print(f"I'm sorry, you need to be at least 25 years old")