#Day 6
#advanced topics
"""
-regular expression
-generators and iteration
-decorators
-context managers
-multithreading and multiprocessing
"""

#Regular expression
"""
\d: matches digits from 0-9
\w: matches any alphanumeric xter(a-z, A-Z, 09, and underscore)
\s: matches any whitespace
.: matches any xter except a newline
*: matches Zero or more occurrences
+: matches One or more occurrences
?: matches Zero or one occurrences
[ ]: matches any xter within the [] brackets
[^ ]: matches any xter not witdin the [] brackects
^: matches start of line
$: matches end of line
"""

#matching and searching
#regex re.match(), re.search(), re.findall(), re.split, re.sub

#Example 1 Demostrating regex | match 1st word, match gp word, match all numbers
import re
text = "Hello, my name is heli. I am a programmer with 25 years of experience"
#Match 1st word
match = re.search(r"^\b\w+\b", text)
if match:
    print("match:", match.group())

matches = re.findall(r"\d+", text)
print("matches:", matches)

match1 = re.split("\s", text)
print(match1)

match2 = re.sub("\s", "9", text)
print(match2)

#Example 2 validate email format/address
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = "heli.pj02@gmail.com"
email2 = "heli.pj02@gmailcom"

print(validate_email(email1))
print(validate_email(email2))

# Genrators and iterators
# 'yield' generator
def fact(n):
    if n == 0:
        yield 1
    else:
        f1 = 1
        for i in range(1, n+1):
            f1 *= i
            yield f1

for i in range(1,10):
    print(*fact(i))

#Decorators @my_decorator
#allowa u to modify behaviour of funs/classes without directly changing their source code
# def my_decorator(func):
#     def inner():
#         print("this is decorator")
#         func()
#     return inner


# @my_decorator
# def outer_decorator():
#     print('this is outer decorator')

# outer_decorator()

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print ("This is my decorator before function execution")
        result = func(*args, **kwargs)
        print ("After function execution" )
        # Code to execute after the oríginal function return result
        return result
    return wrapper
@my_decorator 
def my_function():
    print("Inside the function" )
my_function()




