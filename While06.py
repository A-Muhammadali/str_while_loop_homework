def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if s[k].lower()=="e" or s[k].lower()=="i" or s[k].lower()=="a" or s[k].lower()=="u" or s[k].lower()=="o":
            n=n+1
        k=k+1
    return len(s)-n
print(main("CodeschoolUz"))