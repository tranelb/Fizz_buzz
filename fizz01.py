print "fizz buzz counting up to 100"
for x in range(1,100):
#    if x%3 != 0:
    if x%3 == 0:
        print "fizz"
    elif x%5 == 0:
        print "buzz"
    else:
        print x
