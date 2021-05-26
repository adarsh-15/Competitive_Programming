# cook your dish here

def worldRecord(a,b,c,d):
    if round(100/(a*b*c*d),2) < 9.58:
        print('YES')
    else:
        print('NO')
        


def main():
    t = int(input())
    for i in range(t):
        (a,b,c,d) = map(float,input().split(' '))
        worldRecord(a,b,c,d)

if __name__ == '__main__':
    main()