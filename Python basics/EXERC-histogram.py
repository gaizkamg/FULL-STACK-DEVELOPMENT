'''
We must create a histogram or chartbar graph symbolizing the sales of the different companies, something like this:

g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$

g= google
f= facebook
t= twitter
o= offline

'''
#first we need a diccionary of the sales

sales ={
    'Google': 20,
    'Facebook' : 42,
    'Twitter' : 10,
    'Offline' : 12,
}

#We convert the numbers into symbols and then print them out on console
 
for i in sales:
    # sales_keys[i] i represents each element of the dictionary. So we are selecting the first letter of the 'name' with the range [:1] and then make them lowercaps
    print((i[:1].lower()) + ' = ' + (sales[i])*'$')
