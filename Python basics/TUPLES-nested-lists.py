post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,) #this will add the list tags as the last element of post tuple

print(post) #this will throw the entire tuple
print(post[-1][2]) #this will access to the last element of the tuple [-1] and then the 3rd element of the list [2] >> tutorial