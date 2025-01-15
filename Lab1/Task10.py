#it is from "Python string"
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#it is from "slicing strings"
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2])

#it is from "modify strings"
a = "Hello, World!"
print(a.lower())
a = "Hello, World!"
print(a.upper())
a = " Hello, World! "
print(a.strip()) 
a = "Hello, World!"
print(a.split(","))

#it is from "concatanate strings"
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#it is from "fromat strings"
price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)

#it is from "escape characters"
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#it is from "string methods"
s = "abc123"
print(s.isdigit())
print(s.isalnum)
print(s.capitalize)
print(s.find(a))