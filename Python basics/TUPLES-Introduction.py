# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# List: mutable
post_list = ['Python Basics', 'Intro guide to python', 'Some cool python content']




# Tuple unpacking
title, sub_heading, content = post
print('TUPLES: -------------------')
print('Title: ' + title)
print('SubHeading: ' + sub_heading)
print('Content: ' + content)

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

# Sorting alphabetically
post_list.sort()

# List unpacking with a new order >> title=Intro...   sub_heading=Some cool...    content=Python... 
# That's not a desirable behavior
title, sub_heading, content = post_list
print('LISTS: -------------------')
print('Title: ' + title)
print('SubHeading: ' + sub_heading)
print('Content: ' + content)

#If we try to do the same with the tuple, will drop an error
# post.sort()        # output >>> AttributeError: 'tuple' object has no attribute 'sorted'
title, sub_heading, content = post
print('TUPLES: -------------------')
print('Title: ' + title)
print('SubHeading: ' + sub_heading)
print('Content: ' + content)

#Check the ID of the tuple so we can check if it's the same or another one
print('ID:',id(post)) #30572872



