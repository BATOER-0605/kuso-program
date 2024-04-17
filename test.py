import ctypes as ct

cfile = ct.cdll.LoadLibrary("test")

cunko = cfile.unko

cunko.argtypes = ct.c_int , ct.c_float , ct.c_double
cunko.restype = ct.c_int

def execute(test):
    cunko(test)