
print("Hello, world! NO YAY")


# median function
import math
def median(input):
  length=len(input)
  if length % 2 == 0:
    return((input[math.floor(length / 2)-1]+input[math.floor(length / 2)])/2)
  else:
    return (input[math.floor(length/2)])

# test
my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))

# testing the median switch