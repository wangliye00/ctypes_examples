import ctypes

def main():
    lib = ctypes.cdll.LoadLibrary('MyDLL.dll')
    add = lib.add
    add.argtypes = (ctypes.c_int, ctypes.c_int)
    add.restype = ctypes.c_int
    rst = add(10,4)
    print(rst)
    
if __name__ == '__main__':
  main()
