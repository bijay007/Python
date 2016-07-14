big = None
tiny = None
print '***  Enter the word exit if you want to quit  ***'
print 
while True:
    number = raw_input('Enter an integer: ')
    if number == "exit":
            break
    try:
        number = float(number)
    except:
        print "Invalid input. Only numbers accepted. Try again"
        continue
    if big is None or tiny is None:
	    big = number
	    tiny = number
    if number > big: 
        big = number
    if number < tiny:
        tiny = number
print 'Maximum is ', big
print 'Minimum is ', tiny
input("Press any key to exit :")

