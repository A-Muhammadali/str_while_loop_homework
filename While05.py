def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    k=0
    while k!=len(s):
        if s[k].lower()==s[k]:
            n=n+1
        k=k+1
    return n
print(main("Ust"))