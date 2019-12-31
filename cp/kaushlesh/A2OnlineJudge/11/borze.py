code = input()

zero = '.'
one = '-.'
two = '--'

code = code.replace(two, '2')
code = code.replace(one, '1')
code = code.replace(zero, '0')

print(code)