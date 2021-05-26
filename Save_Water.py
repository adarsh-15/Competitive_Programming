# cook your dish here
def isEnough(a,b,c,d):
    tot = b + int(c/2)
    tot_usage = tot*a 
    if tot_usage == d or tot_usage < d:
        return "YES"
    return "NO"




def main():
    for i in range(int(input().strip())):
        (a,b,c,d) = map(int,input().strip().split(' '))
        print('{0}'.format(isEnough(a,b,c,d)))




if __name__ == "__main__":
    main()