m = raw_input("enter a number: ")
t = int(m)

print "fizz buzz counting up to " + m
for x in range(1,t):
#    if x%3 != 0:
    if x%3 == 0:
        print "fizzy"
    elif x%5 == 0:
        print "buzzy"
    else:
        print x
