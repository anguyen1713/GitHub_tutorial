print("Hello World! The weather sucks.")


# median func
import math

def median(input2):
  list1=len(input2)
  if len(input2) % 2 == 0:
    return((input2[math.floor(list1 / 2)-1]+input2[math.floor(list1 / 2)])/2)
  else:
    return (input2[math.floor(list1/2)])

# mean func
def mean(input):
  tot = 0
  for entry in input:
    tot += entry
  return tot / len(input)

# list
my_list = [0, 1, 2, 3, 4, 5]
# test mean func
print(mean(my_list))
# testing median func
print(median(my_list))

