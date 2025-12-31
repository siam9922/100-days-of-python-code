#Instructor Notes
#------------------------------------------------------------------------------------------

# Figure out how to pick a random name from the list of friends.

#  Hint 1 
# There are two ways of doing this and they are equally valid.
#  Hint 2 
# Think about how you can generate random number to use an index to pick out items from the List.
#  Hint 3 
# Alternatively think about using the documentation to figure out how to get a random item from a List in Python.

#------------------------------------------------------------------------------------------

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
name = random.randint(1, 5)

if name == 1:
    friends = friends[0]
    print("Alice")
elif name == 2:
    friends = friends[1]
    print("Bob")
elif name == 3:
    friends = friends[2]
    print("Charlie")
elif name == 4:
    friends = friends[3]
    print("David")
else:
    print("Emanuel")

#Alternate options


#Use Google
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))

#Use what we learned
# random = random_index = random.randint(0, 4)
# print(friends[random_index])