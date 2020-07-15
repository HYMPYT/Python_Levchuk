def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence"""
    N = len(X)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
        print(f"~~~~~~~~ i = {i} ~~~~~~~~~~")
        lo = 1
        hi = L
        while lo <= hi:
            print(f"lo = {lo}; hi = {hi}")
            mid = (lo + hi) // 2
            print(f"mid = {mid}: {X[M[mid]]} < {X[i]}")
            if (X[M[mid]] < X[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        print(f"newL = {newL}")
        P[i] = M[newL - 1]
        M[newL] = i
        print(f"X = {X}")
        print(f"P = {P}")
        print(f"M = {M}\n")
    
        if (newL > L):
            L = newL
 
    S = []
    k = M[L]
    print()
    for i in range(L - 1, -1, -1):
        print(f"k = {k}")
        S.append(X[k])
        print(f"S = {S}")
        k = P[k]
    return S[::-1]

def my_lst(string):
    lst = string.split(' ')
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst
 
if __name__ == '__main__':
    string = input("Enter a sequence of numbers delimited by space -> ")
    nums = my_lst(string)
    print("Input ->", nums)
    print("Output ->", longest_increasing_subsequence(nums))