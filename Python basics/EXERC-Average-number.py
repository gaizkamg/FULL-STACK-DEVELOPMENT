num_list = [9,2,5,48,5,0.6]

def average(list):
    total_elements = len(list)
    suma = 0
    for numero in list:
        suma = suma + numero 
    a_number = suma / total_elements
    
    return a_number

print(average(num_list))