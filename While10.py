def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if int(s[k])%2==1:
            n=n+int(s[k])
        k=k+1
    return n
print(main("589765"))