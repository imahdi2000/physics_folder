m = 0
kg = 0

def run():
    global m
    m = input('Enter diameter of tube in meters: ')
    global kg
    kg = input('Enter mass of object in kg: ')
    while(True):
        print "New Trial-------------------------------------"
        s = input('Enter seconds: ')
        h = input('Enter height in meters: ')
        print " Speed: " + str(speed(s))
        print ".5mv^2: " + str(kenergy(s))
        print "  -^PE: " + str(penergy(h))
        print "Dispan: " + str(edis(s,h))
        print " ratio: " + str(ratio(s,h))

def speed(s):
    return (m/s)

def kenergy(s):
    v = speed(s)
    return .5 * kg * (v*v)

def penergy(h):
    return kg  * 9.81 *  h

def edis(s,h):
    return penergy(h) - kenergy(s)

def ratio(s,h):
    return (edis(s,h))/(penergy(h)) * 100

run()
