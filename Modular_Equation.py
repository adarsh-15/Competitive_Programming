

def modEquation(n,m,fact):
    ans = 0

    

    for b in range(2,n+1):
        t = m - m%b
        if b > m:
            ans += b-1
        else:
            f = fact[t]
            st = 0
            en = len(f) - 1
            while st <= en:
                mid = (st+en)//2
                if f[mid] < b:
                    st = mid+1
                else:
                    en = mid-1 
            ans += st

    return ans
        
    
def main():
    fact_s = int(5.e5)+1
    fact = [[]*fact_s for i in range(fact_s)]
    
    for i in range(1,fact_s):
        for j in range(i,fact_s,i):
            fact[j].append(i)
    for i in range(int(input().strip())):
        n,m = map(int,input().strip().split(' '))
        print('{0}'.format(modEquation(n,m,fact)))


if __name__ == "__main__":
    main()