"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list= sorted(sale_prices)
print(sorted_list) # [1, 3, 10, 40, 83, 100, 100, 220, 400]

list_lengh= len(sorted_list)
print(list_lengh) #9

half_lengh= math.floor(list_lengh/2)
print(half_lengh) #4

median = sorted_list[half_lengh:(half_lengh+1)]
print(median) #[83]

index_of_40 = sorted_list.index(40)
print(index_of_40)




