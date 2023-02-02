# Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)

# Private instance attribute: width:
# property def width(self): to retrieve it
# property setter def width(self, value): to set it:
# width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
# if width is less than 0, raise a ValueError exception with the message width must be >= 0
# Private instance attribute: height:
# property def height(self): to retrieve it
# property setter def height(self, value): to set it:
# height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
# if height is less than 0, raise a ValueError exception with the message height must be >= 0
# Public class attribute number_of_instances:
# Initialized to 0
# Incremented during each new instance instantiation
# Decremented during each instance deletion
# Public class attribute print_symbol:
# Initialized to #
# Used as symbol for string representation
# Can be any type
# Instantiation with optional width and height: def __init__(self, width=0, height=0):
# Public instance method: def area(self): that returns the rectangle area
# Public instance method: def perimeter(self): that returns the rectangle perimeter:
# if width or height is equal to 0, perimeter has to be equal to 0
# print() and str() should print the rectangle with the character #:
# if width or height is equal to 0, return an empty string
# repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
# Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
# Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
# rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
# rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
# Returns rect_1 if both have the same area value
# You are not allowed to import any module
# guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")