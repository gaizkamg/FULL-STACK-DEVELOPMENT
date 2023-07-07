tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2] #from index 1 to the last element (-1) skipping 
print('tags[1:-1:2]: ', tag_range)
tag_range = tags[::-1] # from 0 to the end in reverse 
print('tags[1:-1:2]: ', tag_range)

print('tags[::-1]: ', tag_range)

tags.sort(reverse=True)

print('sorted alphabetically: ', tags)
