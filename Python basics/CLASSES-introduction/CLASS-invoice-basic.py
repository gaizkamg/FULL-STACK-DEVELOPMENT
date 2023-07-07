class Invoice:

    def greeting(self):
        return 'Hi there'

inv_one = Invoice()
print(inv_one) # <__main__.Invoice object at 0x004F1950>

inv_two = Invoice()
print(inv_two) # <__main__.Invoice object at 0x007C15F0>

#if we want the Invoice to use the greeting function>>

print(inv_one.greeting()) # Hi there

