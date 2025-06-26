
print("Hello, world! NO YAY")


# mean function
def mean(input):
    tot=0
    for entry in input:
        tot += entry
    return tot/len(input)

# test
my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))

# testing the branch stuff
