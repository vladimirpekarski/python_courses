__author__ = 'vladimir.pekarsky'

def h(x, y, *args, **kwargs):
    print("x={}, y={}, args={}, kwargs={}".format(x, y, args, kwargs))


h(1, 2, 3, 4, 5, 6, 7, z='j', t='s')
