'''
remove_first_and_last(list_to_clean)
html= ['<h1>', 'Some content', '</h1>']

remove_first_and_last(html)
>> 'Some content'
'''

#setting up the list

html= ['<h1>', 'Some content', 'another content', 'great things', '</h1>']

#defining the function
 
def remove_first_and_last(list_to_clean):
    list_elements = len(list_to_clean) #getting the number of elements
    # print(list_elements)
    # cleaned_list = list_to_clean[1:(list_elements)-1]
    return list_to_clean[1:(list_elements)-1] #slicing the list

print(remove_first_and_last(html))

#another approach to the resolution using iterable unpacking. If you assing a list of variables with the * in the middle of the option, it will catch the first one, 
def remove_1st_last(list_to_clean):
    first, *content, last =  list_to_clean
    return content

print(remove_1st_last(html))