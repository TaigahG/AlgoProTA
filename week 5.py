def times(n1,op,n2):
    return n1*n2
def divide(n1,op,n2):
    return n1/n2
def plus(n1,op,n2):
    return n1+n2
def minus(n1,op,n2):
    return n1-n2




def cal(n1,op,n2):
    if op == "*":
        print(times(n1,op,n2))
    if op == "/":
        print(divide(n1,op,n2))
    if op == "+":
        print(plus(n1,op,n2))
    if op == "-":
        print(minus(n1,op,n2))
chck = True
while chck == True:
           
    n1 = int(input("enter num: "))
    op = input("enter operator: ")
    n2 = int(input("enter num: "))
    cal(n1,op,n2)
    if (input("continue?(y/n) ")) != "y":
        break

        
        
