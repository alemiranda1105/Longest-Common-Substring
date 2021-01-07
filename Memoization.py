

def memoization(s1, s2):
    mem = {}

    def getKey(l1, l2):
        key = str(l1) + "|" + str(l2)
        return key

    def findLengthLCS(mem, s1, s2, l1, l2):
        if l1 == len(s1) or l2 == len(s2):
            return 0
        key = getKey(l1, l2)
        if key not in mem:
            if s1[l1] == s2[l2]:
                mem[key] = 1 + findLengthLCS(mem, s1, s2, l1+1, l2+1)
            else:
                mem[key] = max(findLengthLCS(mem, s1, s2, l1+1, l2), findLengthLCS(mem, s1, s2, l1, l2+1))
        return mem[key]

    return findLengthLCS(mem, s1, s2, 0, 0)
