class Invoice:

    def  __init__(self, client, total):
        self.client = client
        self.total = total
    
    def formatter(self):
        return f'{self.client} owes ${self.total}'

google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())

print('get client value:', snapchat.client)


print('before set: ', google.client)

google.client = 'Yahoo'

print('after set: ',google.client)


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # use underscore to indicate it's a private variable
    
    @property
    def age(self):
        return self._age

class Demon:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # use underscore to indicate it's a private variable
     

p = Person('Gaizka', 45)
print(p.age)

d = Demon('Baal', 10293)
print(d.age)


