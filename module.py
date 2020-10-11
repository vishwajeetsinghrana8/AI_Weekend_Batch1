def func1():
    print("This is python first function")
    
def func2():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))
    var3 = var2+var1
    print("Addition:",var3)
    
def func3(var1,var2):
    var3 = var1 *var2
    print("Multiply:",var3)
    
def func4():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))    
    var3 = var1 ** var2    
    return var3

def func5(var1,var2):
    var3 = var1/var2
    return var3,var1