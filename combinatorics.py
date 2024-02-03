# Aprogram to find the pernutation and combination
def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def permutation(n, r):
    return factorial(n)//factorial(n-r)

def combination (n, r):
    return factorial(n)//((factorial(n-r)*factorial(r)))

def main():
    print(combination(52,5))

main()
    
    
