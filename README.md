
##Lab Work 2-1

<b> Write the code to do following:  </b>   
    <div>
        <ol>
            <li>Create any variable with name var1</li>
            <li>Check type of var1 with type function</li>
            <li>Check is var1 is True</li>
            <li>Check is var1 is False </li>
            <li>Create var2 that equal to (var1 or True) </li>
            <li>Check is var2 is True  </li>
            <li>Check is var2 is False </li>
            <li>Check result for var2 and var1</li>
         </ol>   
     </div>
</b>
<h6> Code </h>  

```python
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

```



##Lab Work 2-2

<b> Write the code to do following:  </b>   
    <div>
        <ol>
            <li>Generate sequence 5 integers long from range(0, 100) </li>
            <li>Generate random float </li>
            <li>Print variables above </li>
            <li>Find max element from generated sequence </li>
            <li>Make a floor division between max element and generated float </li>
            <li>Find factorial of the result above </li>
            <li>Shorten the code as much as possible </li>
         </ol>   
     </div>
</b>
<h6> Code </h>  

```python
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
```
