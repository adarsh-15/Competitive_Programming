# cook your dish here
def dist_Choc(n,x,a):
    a_set = set(a)
    a_fin = list(a_set)
    if len(a)-len(a_fin) >= x:
        return len(a_fin)
    return len(a)-x
    


def main():
    for i in range(int(input().strip())):
        n, x = map(int,input().strip().split(' '))
        a = list(map(int,input().strip().split(' ')))
        print('{0}'.format(dist_Choc(n,x,a)))

if __name__ == '__main__':
    main()