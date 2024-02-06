def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    l = [int(i) for i in str(x).strip("-")]
    length = len(l)
    for i in range(int(length / 2)):
        print(l[i], l[length - 1 - i])
        if l[i] != l[length - 1 - i]:
            return False
    return True


def isPalindromeOneLiner(x: int) -> bool:
    l = str(x)
    return (
        False if x < 0 else all(l[i] == l[len(l) - 1 - i] for i in range(len(l) // 2))
    )
