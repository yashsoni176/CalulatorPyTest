def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def div(x,y):
    return x/y

if __name__ == "__main__":
    num1 = float(input("Enter a : "))
    num2 = float(input("ENTER b : "))
    result1 = add(num1, num2)
    print(result1)
    result2 = sub(num1, num2)
    print(result2)
    result3 = multi(num1, num2)
    print(result3)
    result4 = div(num1, num2)
    print(result4)
