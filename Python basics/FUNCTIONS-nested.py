def full_name(first, last):
    return f'{first} {last}'

def greeting(name):
    print(f'Hi, {name}!')

Gaizka = full_name('Bruce', 'Waine')
greeting(Gaizka)

#we can nest a function inside another



def greeting_nested(first, last):

    def full_name():
        return f'{first} {last}'
    
    print(f'Hi, {full_name()}!')

greeting_nested('Gaizka','Martinez')

