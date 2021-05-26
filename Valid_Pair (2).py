# cook your dish here
def socks(a,b,c):
    if a == b:
        print('YES')
    elif a==c:
        print('YES')
    elif b == c:
        print('YES')
    else:
        print('NO')

def main():
    (a,b,c) = map(int,input().split(' '))
    socks(a,b,c)


if __name__ == '__main__':
    main()
