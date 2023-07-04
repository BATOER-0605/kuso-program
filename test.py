import ctypes as ct

cfile = ct.cdll.LoadLibrary("test")

cunko = cfile.unko

cunko.argtypes = None
cunko.restype = ct.c_int

cres = cunko()

print(cres)