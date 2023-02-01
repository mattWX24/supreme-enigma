def calculate(expression):
    # Eval the expression using built-in eval function
    result = eval(expression)
    return result


# Get an expression from the user
expression = input('Enter an expression: ')

# Call the calc function and print result
result = calculate(expression)
print('Result: ', result)
