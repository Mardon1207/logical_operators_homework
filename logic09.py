def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return a%2==1 or b%2==1
a=int(input())
b=int(input())
print(main(a,b))