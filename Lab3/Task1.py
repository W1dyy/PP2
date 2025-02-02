def my_func():
    print("Hello world")


my_func()


def name(x, y):
    print(x + " " + y)


name("Amir", "Omar")


def my_functio(*kids):
  print("The youngest child is " + kids[1])

my_functio("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")




def my_food(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_food(fruits)


def my_combo(x):
  return 5 * x

print(my_combo(3))
print(my_combo(5))
print(my_combo(9))


def my_func(x, /): # ,/ can use only by inputing arguments as 3, 4, 5, 6.... Cant input x = 3 and etc.
  print(x)

my_func(3)


def my_func(*, x): # *, can use only by inputing meaning of variable. For example x = 7.
  print(x)

my_func(x=3)


def my_var(a, b, /, *, c, d):
  print(a + b + c + d)

my_var(5, 6, c = 7, d = 8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

