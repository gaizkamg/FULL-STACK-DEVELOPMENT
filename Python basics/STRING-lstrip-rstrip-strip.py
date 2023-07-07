url = '             https://google.com          ' #strip will remove the spaces before and after the string
url = url.strip()
print(url)

url = url.lstrip('https://') # lstrip will remove the left element that we pass through the argument
print(url)
url = url.rstrip('.com') # rstrip will remove the right element that we pass through the argument

print(url.capitalize())