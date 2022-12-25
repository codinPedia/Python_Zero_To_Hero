################# Falsy Values #################
### Numbers - Zero of any numeric type
# Integer: 0
# Float: 0.0
# Complex: 0j

### Sequences and Collections
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)

### Constants
# None
# False
################################################

### 1
a = 10
b = 5
print(id(a))
print(id(b))
print(a is b)

### 2
c = "Codin"
c += "Pedia"
d = "CodinPedia"

print(c)
print(d)

print(id(c))
print(id(d))

print(c == d)
print(c is d)
print(id(c) == id(d)) # id(c) == id(d) same as c is d

x = None
if x is None:
    print("It Is None!")

if bool(x) == False: # Same as -> if not x:
    print("It Is Falsy!")
