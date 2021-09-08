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
    # The above condition: __name__=="__main__", allows this file to do double duty.  
    # 1) It can act as a package defining functions or classes above that can be imported by other python files
    #    When functions or classes are imported, what is after this condition is ignored.
    # 2) This file can run in a debugger or called directly using: python filename.py
    #    In this case all the classes / functions above are first defined, and then the code below is also executed.
    #    This is convenient for testing and debugging functions defined above.  For example, call the following from the command line:
    #    python arithmetic.py
    
    a, b = 3, 4
    print(f"Testing multiply({a},{b}) = {multiply(a,b)}")

    n = 5
    print(f"Testing sum_to_n({n}) = {sum_to_n(n)}")
