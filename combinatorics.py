# Aprogram to find the pernutation and combination
def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def permutation(n, r):
    return factorial(n)//factorial(n-r)

def main():
    print(permutation(5,2))

main()
    
    
