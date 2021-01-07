

def memoization(s1, s2):
    mem = {}

    def getKey(l1, l2, count):
        key = str(l1) + "|" + str(l2) + "|" + str(count)
        return key

    def findLengthLCS(mem, s1, s2, l1, l2, count):
        if l1 == len(s1) or l2 == len(s2):
            return count
        key = getKey(l1, l2, count)
        if key not in mem:
            c1 = count
            if s1[l1] == s2[l2]:
                c1 = findLengthLCS(mem, s1, s2, l1+1, l2+1, count+1)
            c2 = findLengthLCS(mem, s1, s2, l1, l2+1, 0)
            c3 = findLengthLCS(mem, s1, s2, l1+1, l2, 0)
            mem[key] = max(c1, max(c2, c3))
        return mem[key]

    return findLengthLCS(mem, s1, s2, 0, 0, 0)
