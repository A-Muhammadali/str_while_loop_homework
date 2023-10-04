def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if ("!"<=s[k] and "/">=s[k])or(":"<=s[k] and "@">=s[k])or("["<=s[k] and "`">=s[k])or("{"<=s[k] and "~">=s[k]):
            n=n+1
        k=k+1
    return n
print(main("02k112lkl1j1!@#$%^&*"))
