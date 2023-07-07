tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2] #from index 1 to the last element of the list (-1), and alternating 2 elements. 
print('print-01: ', tag_range)
tag_range = tags[::-1] #from 0 to end, in reverse

print('print-02: ',tag_range)

tags.sort(reverse=True)

print('print-03 reversed: ',tags)