var1 = ("Hello") # string
var2 = ("Hello",) # tuple

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')
#Adding elements to a tuple
post = post + ('published',)

title, sub_heading, content, status = post
print('NEW TUPLE: -------------------')
print('Title: ' + title)
print('SubHeading: ' + sub_heading)
print('Content: ' + content)
print('Status: ' + status)
#As we can see here, in the memory is stored a tuple with an ID and after reasigning with more elements python has created another tuple with the same name
print('ID:',id(post)) #35141168


#Deleting elements from a tuple
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')
print(post)

# Removing elements from end
post = post[:-1]
print(post)

# Removing elements from beginning
post = post[1:]
post = post + ('published',)
post = ('Python Basics',) + post
print(post)

# Removing specific element (messy/not recommended)
# post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')
print('ID origen:',id(post))
post = list(post)
print('ID lista:',id(post))
post.remove('published')
print('ID remove:',id(post))
post = tuple(post)
print('ID tuple:',id(post))
print(post)