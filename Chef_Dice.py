# cook your dish here

def getMaxPip(n):
    ans = 0
    if n<=4:
        if n == 1:
            return 20
        elif n == 2:
            return 36
        elif n == 3:
            return 51
        elif n == 4:
            return 60
    else:
        if n%4 == 1:
            return (int(n/4)-1)*44+60+16
        elif n%4 == 2:
            return (int(n/4)-1)*44+60+28
        elif n%4 == 3:
            return (int(n/4)-1)*44+60+39
        elif n%4 == 0:
            return (int(n/4)-1)*44+60+0
    
    

def main():
    t = int(input().strip())
    for i in range(t):
        num_dice = int(input())
        print('{0}'.format(getMaxPip(num_dice)))




if __name__ == '__main__':
    main()