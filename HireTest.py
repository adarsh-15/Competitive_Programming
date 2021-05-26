# cook your dish here
def passFail(n,x,y,z):
    f = 0
    p = 0
    u = 0
    for i in z:
        if i == 'F':
            f += 1
        elif i == 'P':
            p += 1
        elif i == 'U':
            u += 0
    if f >= x or (f>= x-1 and p >= y):
        return 1 
    return 0
        
    


def main():
    for i in range(int(input().strip())):
        n,m = map(int,input().strip().split(' '))
        x,y = map(int,input().strip().split(' '))
        st = ''
        for i in range(n):
            z = input().strip()
            temp = passFail(n,x,y,z)
            st += str(temp)
        print(st)
            
            


if __name__ == "__main__":
    main()
