def main():
    x,y=input_numbers()
    summation = add(x,y)
    display(x,y,summation)

def input_numbers():
    x,y=input("Enter two numbers: ").split()
    x,y=[int(x),int(y)]
    return x,y

def add(x,y):
    return x+y

def display(x,y,sum):
    print("The sum of {0} + {1} = {2}".format(x,y,sum))

main()
