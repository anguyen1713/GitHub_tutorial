print("Hello World! The weather sucks.")

# median func
import math

def median(input):
  list1=len(input)
  if len(input) % 2 == 0:
    return((input[math.floor(list1 / 2)-1]+input[math.floor(list1 / 2)])/2)
  else:
    return (input[math.floor(list1/2)])

# testing median func
print(median(my_list))