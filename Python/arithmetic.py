def multiply(x, y):
    """ Returns the product of x and y """
    result = x * y
    return result

def sum_to_n(n):
    """ Finds sum of integers from 0 to n inclusive """
    i = 0
    sum_val = i
    while i <= n:
        sum_val += i
        i += 1
    return sum_val

if __name__ == "__main__":
    
    a, b = 3, 4
    print(f"Testing multiply({a},{b}) = {multiply(a,b)}")

    n = 5
    print(f"Testing sum_to_n({n}) = {sum_to_n(n)}")
