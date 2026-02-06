
num = int(input("enetr the number:-"))

def factorial(num):
    factorial =1
    for i in range(1, num+1): 
     factorial *=i
                        
    return factorial


fac_result = factorial(num)

print("factorial of num is=", fac_result)
