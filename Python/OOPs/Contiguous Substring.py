word = "abcab"

def Con_substring(x):
    length = len(x)
    count = 0
    for i in range(length):
        # print(x[i])
        for j in range(i,length):
            if x[i] == x[j]:
                count += 1
    return count

print(Con_substring(word))
