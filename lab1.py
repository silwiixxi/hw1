#101
name = input()
print("Hello, " + name + "!")

#102
a = input()
b = input()
print(a, b, sep="***")

#103
s = input()
if s.isdigit():
    print("int")
else:
    print("str")

#104
a = int(input())
b = int(input())
print(a + b)

#105
a = int(input())
b = int(input())
print(a // b)
print(a / b)

#106
a = int(input())
b = int(input())
print(a ** b)

#107
a = int(input())
b = int(input())
print(a % b)

#108
s = input()
n = int(input())
print(s * n)

#109
text = input()
print(len(text))

#110
s = input()
print(s.upper())
print(s.lower())

#111
s = input()
print(s[0], s[-1])

#112
s = input()
print(s[2:5])

#113
s = input()
print(s[::-1])

#114
name = input()
age = int(input())
print(f"Hello, {name}. You are {age} years old.")

#115
long_str = input()
short_str = input()
print(short_str in long_str)

#116
a = input()
b = input()
print(a + b)

#117
a = input()
b = input()
print(b, a)

#118
n = int(input())
if n % 2 == 0:
    print("even")
else:
    print("odd")

#119
s = input()
old = input()
new = input()
print(s.replace(old, new))

#120
a = int(input())
b = int(input())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("equal")