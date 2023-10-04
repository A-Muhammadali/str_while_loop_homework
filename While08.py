def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if int(s[k])%2==1:
            n=n+1
        k=k+1
    return n
print(main("1567534"))