
try:
   open("file.tex")
except NameError:
    print("NameError exception is thrown because the variable is not defined")
except ArithmeticError:
    print("ArithmeticError exception is thrown.")
except FileNotFoundError:
    print("FileNotFoundError exception is thrown.")




while True:
    try:
        input = int(input("please enter a number : "))
        break
    except:
        print("only numbers are allowed as input , please try again!")