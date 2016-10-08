first = 0; next = 1; sum = 0
ask = input ('Enter a limit to calculate its Fibonacci sequence : ')
if ask > 50: print 'Too large. Enter smaller than 50'
else:
    for i in range (0,ask):
        sum = first + next
        first = next
        next  = sum
        print sum
        sum = 0
