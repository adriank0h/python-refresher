def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divided by zero error")
        raise TypeError("A type error occurred")
        raise ValueError("A value error occurred")
    return dividend / divisor


grades = [] # Imagine we have no grades yet
print('welcome to the average grade programme')


try:
    average = divide(sum(grades), len(grades))
    

except ZeroDivisionError as e:
    print(e)
    # Much friendlier error message because now we're dealing with it
    # In a "students and grades" context, not purely in a mathematical context
    # I.e. it doesn't make sense to put "There are no grades yet in your list"
    # inside the `divide` function, because you could be dividing something
    # that isn't grades, in another program.
    print("There are no grades yet in your list.")
else:
    print(str(average) + ' is the average grade')
finally:
    print('Thank you for using the average grade programme')

