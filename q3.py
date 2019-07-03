def sortStringArray(s, a, n):

    # Sort the array according to the new alphabetical order
    a = sorted(a, key = lambda word: [s.index(c) for c in word])
    for i in a:
        print(i, end =' ')

# Driver code
s = "rcta"
a = ["car", "rat", "cat"]
n = len(a)
sortStringArray(s, a, n)
