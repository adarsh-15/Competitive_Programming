# cook your dish here


def bitXor(n):
    ans = 1
    y = n-1
    x = 2
    k = (pow(10,9)+7)
    x = x%k
    
    while y > 0:
        if y%2 != 0:
            ans = (ans*x)%k 
        
        y = y//2
        x = (x*x)%k 
        
    return ans
    
    



def main():
    for i in range(int(input().strip())):
        n = int(input().strip())
        print('{0}'.format(bitXor(n)))


if __name__ == '__main__':
    main()
