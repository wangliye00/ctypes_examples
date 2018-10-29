import ctypes

#! When call shared library, you should define datatype of args by argtypes, 
#! and data type of return value by restype. Set restype to None if there's no return value. \

class DoubleArrayType(object):
    def __init__(self):
        super(DoubleArrayType, self).__init__()
    
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("failed to convert from %s" %typename)
    
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr,_ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))
    
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val
    
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

def main():
    lib = ctypes.cdll.LoadLibrary('MyDLL.dll')
    add = lib.add
    add.argtypes = (ctypes.c_int, ctypes.c_int)
    add.restype = ctypes.c_int
    rst = add(10,4)
    print(rst)
    
    #! pass customized object to function\
    _avg = lib.avg
    _avg.argtypes = (DoubleArrayType(), ctypes.c_int)
    _avg.restype = ctypes.c_double
    
    import numpy as np
    data = np.array([1.0,2.0,3.0])
    rst = _avg(data, len(data))
    print(rst)
    
if __name__ == '__main__':
  main()
