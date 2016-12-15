'''
1. Generate sequence 5 integers long from range(0, 100)
2. Generate random float
3. Print variables above
4. Find max element from generated sequence
5. Make a floor division between max element and generated float
6. Find factorial of the result above
7. Shorten the code as much as possible
'''
import random
import math

# 1. Generate sequence 5 integers long from range(0, 100)
var1 = random.sample(range(100), 5)

# 2. Generate random float
var2 = random.random()

# 3. Print variables above
print("var1 = {}, var2 = {}".format(var1, var2))

# 4. Find max element from generated sequence
max_var1 = max(var1)
print("max var1 =", max_var1)

# 5. Make a floor division between max element and generated float
print("max_var1 // var1 {}".format(max_var1 // var2))

# 6. Find factorial of the result above
print("factorial", format(math.factorial(max_var1 // var2)))

