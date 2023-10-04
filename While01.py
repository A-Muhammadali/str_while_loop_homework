def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if "0"<=s[k] and "9">=s[k]:
            n=n+1
        k=k+1
    return n
print(main("02k112lkl1j1"))