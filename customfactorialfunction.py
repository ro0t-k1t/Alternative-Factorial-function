__author__ = 'ronanpiercehiggins'

def fact(num):

    if num == 0:

        print "1"

    else:

        arr = [y for y in range(num, -1, -1) if y > 0]

        return reduce(lambda x, y: x*y, arr)

print fact(5)













































