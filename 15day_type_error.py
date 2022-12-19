# The error was a SyntaxError. After the fix our code was executed without a hitch. Let see more error types.
# print 'hello world'

# The type of error was a NameError. We debugged the error by defining the variable name.
print(age)

numbers = [1, 2, 3, 4, 5]
numbers[5]
# In the example above, Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range.

# In the example above, I added an extra s to math deliberately and ModuleNotFoundError was raised. Lets fix it by removing the extra s from math.
import maths

# ZeroDivisionError
1/0
# We cannot divide a number by zero.

# ValueError
int('12a')
# In this case we cannot change the given string to a number, because of the 'a' letter in it.

# ImportError
from math import power
# There is no function called power in the math module, it goes with a different name: pow. Let's correct it:
from math import pow
