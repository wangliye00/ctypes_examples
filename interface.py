import ctypes

#! When call shared library, you should define datatype of args by argtypes, 
#! and data type of return value by restype. Set restype to None if there's no return value. \

def main():
    lib = ctypes.cdll.LoadLibrary('MyDLL.dll')
    add = lib.add
    add.argtypes = (ctypes.c_int, ctypes.c_int)
    add.restype = ctypes.c_int
    rst = add(10,4)
    print(rst)
    
if __name__ == '__main__':
  main()
