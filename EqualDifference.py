def minNumDif(n, num):
    if n <= 2:
        return 0
    freq = 0
    dic = {}
    for i in num:
        dic[i] = 0
    for i in num:
        dic[i] += 1
        if dic[i] > freq:
            freq = dic[i]
    if freq == 1:
        return n-2
    return n-freq


def main():
    for i in range(int(input())):
        n = int(input())
        num = list(map(int, input().split(" ")))
        print("{0}".format(minNumDif(n, num)))


if __name__ == "__main__":
    main()
