'''
Write the code to do following:
1.	Create any variable with name var1
2.	Check type of var1 with type function
3.	Check is var1 is True
4.	Check is var1 is False
5.	Create var2 that equal to (var1 or True)
6.	Check is var2 is True
7.	Check is var2 is False
8.	Check result for var2 and var1
'''

# 1.	Create any variable with name var1
var1 = 10
print("var1 = ", var1)

# 2. Check type of var1 with type function
print("type(var1)", type(var1))

# 3.	Check is var1 is True

print("bool(var1)", bool(var1))

# 4.	Check is var1 is False
print("bool(not var1)", bool(not var1))

# 5.	Create var2 that equal to (var1 or True)
var2 = var1
print("var2 = var1", var2, var1)

# 6.	Check is var2 is True

print("bool(var2)", bool(var2))

# 7.	Check is var2 is False
print("bool(not var2)", bool(not var2))

# 8.	Check result for var2 and var1
print("var1 {}, var2 {}".format(var1, var2))
