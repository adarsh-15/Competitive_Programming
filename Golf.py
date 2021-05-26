# cook your dish here

def isItGolfed(n,x,k):
    
    if x%k == 0:
        return 'YES' 
        
    if ((n-1)-x)%k == 0:
        return 'YES'
            
    return 'NO'


def main():
    for i in range(int(input().strip())):
        n,x,k = map(int,input().strip().split(' '))
        print('{0}'.format(isItGolfed(n+2,x,k)))

if __name__ == "__main__":
    main()
