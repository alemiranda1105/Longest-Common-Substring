# Resolvemos el ejercicio con greedy
def greedy(s1, s2):
    a = len(s1)
    b = len(s2)
    solution = 0
    for i in range(0, a):
        counter = 0
        k = i
        for j in range(0, b):
            if k >= a:
                break
            if s1[k] != s2[j]:
                counter = 0
                k = 1
            else:
                k += 1
                counter += 1
                if counter >= solution:
                    solution = counter
    return solution
