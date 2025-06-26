print("Hello World! The weather sucks.")

# median func
import math

def median(input2):
  list1=len(input2)
  if len(input2) % 2 == 0:
    return((input2[math.floor(list1 / 2)-1]+input2[math.floor(list1 / 2)])/2)
  else:
    return (input[math.floor(list1/2)])

# testing median func
print(median(my_list))