#1 will print the number 5 for the number of food groups.
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 will log an error in the concole because the first function call in the print function is not defined anywhere.
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 will return and print the number 5.
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 will return and print the number 5.
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 will print 5 to the console and will print nothing for x because there is no return value.
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 will print the evauluated results of the two function calls and which will equal 8.
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 will convert the arguments to a string and return and print the concatenated strings.
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 will print the value of "b" to the console and return and print 10 since b < 100 is false and runs the else statement.
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 will return and print 7 if b variable is less than the c variable.
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # returns and prints 7.
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # returns and prints 14.
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # adds the returned results of the two function calls and prints 21.


#10 returns and prints 8.
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 first print call for b will be 500, 2nd print 500, 3rd print 300, 4th print 500.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 first print for b will be 500, 2nd print 500, 3rd print 300, 4th print 500.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 first print for b will be 500, 2nd print 500, 3rd print 300, 4th print 300.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 output: 1, 3, 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 output: 1, 3, 5, 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)