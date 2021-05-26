# cook your dish here


def strongLang(k,s):
    c=0
    m=0
    temp=0
    for i in s:
        if i == '*':
            c += 1
            temp = max(temp,c)
            
        else:
            c = 0
            
    if temp >= k:
        print('YES')
    else:
        print('NO')
    
        


def main():
    t = int(input())
    for i in range(t):
        (n,k) = map(int,input().split(' '))
        s = input()
        strongLang(k,s)


if __name__ == "__main__":
    main()
