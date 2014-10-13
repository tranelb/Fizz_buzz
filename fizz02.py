print "fizz buzz counting up to 100"
for x in range(1,350):
#    if x%3 != 0:
    if x%3 == 0 and x%5 == 0:
        print "fizz buzz"
    elif x%5 == 0:
        print "buzz"
    elif x%3 == 0:
        print "fizz"
    else:
        print x
