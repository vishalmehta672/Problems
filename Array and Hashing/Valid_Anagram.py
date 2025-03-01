def isAnagram(s: str, t: str) -> bool:

    res1 = {}
    res2 = {}
    for i in s:
        if i in res1:
            res1[i] += 1
        else:
            res1[i] = 1

    for i in t:
        if i in res2:
            res2[i] += 1
        else:
            res2[i] = 1

    return res1 == res2


s = "racecar"
t = "carrace"

print(isAnagram(s, t))


# a = ("dssAa")
# b = ("dssA")

# x = sorted(a) == sorted(b)

# print(x)
