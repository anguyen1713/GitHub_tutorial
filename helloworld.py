print("Hello World! The weather sucks.")

# mean
def mean(input):
  tot = 0
  for entry in input:
    tot += entry
  return tot / len(input)

# test mean func
my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))