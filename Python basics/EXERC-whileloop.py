def loop_using_while():
    dog_house = ['brian','pup','blacky','fuffy'] # Put dog names here
    counter = 0
    
    while counter < 4:
        print(counter)
        print(dog_house[counter])
        counter += 1
    return [dog_house, counter]

print(loop_using_while())