def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if ("A"<=s[k] and "X">=s[k])or("a"<=s[k] and "x">=s[k]):
            n=n+1
        k=k+1
    return n
print(main("02k112lkl1j1"))