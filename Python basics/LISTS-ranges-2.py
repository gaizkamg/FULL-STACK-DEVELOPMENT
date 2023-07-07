tags = ['python', 'development', 'tutorials', 'code']
print(tags)

tag_range = tags[2:]
print('tag[2:] : ',tag_range) # starts in index 2 until the end ['tutorials', 'code']
tag_range = tags[0:2]
print('tag[0:2] : ',tag_range) # starts in index 0 until index 2 ['python', 'development']
tag_range = tags[:2]
print('tag[:2] : ',tag_range) # starts in index 0 until index 2 ['python', 'development']
tag_range = tags[0:-1]
print('tag[0:-1] : ',tag_range) # starts in index 0 until the (-1) first element beggining from the end ['python', 'development', 'tutorials']

print(tag_range)





