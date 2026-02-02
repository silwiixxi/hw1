#DATA TYPES
x = 5
print(type(x))

x = "Hello World"	#str
print(x)
print(type(x)) 


x = 20		#int
print(x)
print(type(x)) 

x = 20.5	#float
print(x)
print(type(x)) 

x = 1j		#complex
print(x)
print(type(x)) 

x = ["apple", "banana", "cherry"]	#list	
print(x)
print(type(x)) 

x = ("apple", "banana", "cherry")	#tuple	
print(x)
print(type(x)) 

x = range(6)	#range	
print(x)
print(type(x)) 

x = {"name" : "John", "age" : 36}	#dict
print(x)
print(type(x)) 

x = {"apple", "banana", "cherry"}	#set
print(x)
print(type(x)) 

x = frozenset({"apple", "banana", "cherry"})	#frozenset	
print(x)
print(type(x)) 

x = True	#bool	
print(x)
print(type(x)) 

x = b"Hello"	#bytes
print(x)
print(type(x)) 

x = bytearray(5)	#bytearray	
print(x)
print(type(x)) 

x = memoryview(bytes(5))	#memoryview	
print(x)
print(type(x)) 

#NUMBERS
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

import random
print(random.randrange(1, 10))

#CASTING
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

#STRING
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x) 

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) #returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 



