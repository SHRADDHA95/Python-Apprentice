
try:
    print(1/0)
except NameError:
    print("NameError exception is thrown because the variable is not defined")
except ArithmeticError:
    print("ArithmeticError exception is thrown")
