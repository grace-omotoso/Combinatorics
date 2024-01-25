# Aprogram to find the pernutation and combination
def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def main():
    print(factorial(5))

main()
    
    
