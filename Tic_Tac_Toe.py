def ticTacToe(lst):
    x, o, d = 0,0,0
    for i in range(3):
        
        for j in lst[i]:
            if j == 'X':
                x += 1 
            elif j == 'O':
                o += 1
            elif j == '_':
                d += 1

    dif = x-o
    #Based On number Of X and O            
    if abs(dif) > 1 or o > x:
        return 3
    
    if x < 3:
        return 2


    m, n = 0, 0

    temp_x = 0
    temp_o = 0
    #First Diagonal Cases
    for i in range(3):
        
        if lst[i][i] == 'X':
            temp_x += 1
        elif lst[i][i] == 'O':
            temp_o += 1

    if temp_x == 3:
        m += 1
    if temp_o == 3:
        n += 1
    
    #Second Diagonal
    temp_x = 0
    temp_o = 0
    
    for i in range(3):
        
        if lst[i][2-i] == 'X':
            temp_x += 1
        elif lst[i][2-i] == 'O':
            temp_o += 1

    if temp_x == 3:
        m += 1
    if temp_o == 3:
        n += 1

    #Horizontal check    

    for i in range(3):
        st = lst[i][0]
        if lst[i][1] == st and lst[i][2] == st and st == 'X':
            m += 1
        elif lst[i][1] == st and lst[i][2] == st and st == 'O':
            n += 1
        
    #Vertical Check

    for j in range(3):
        st = lst[0][j]
        if lst[1][j] == st and lst[2][j] == st and st == 'X':
            m += 1
        elif lst[1][j] == st and lst[2][j] == st and st == 'O':
            n += 1

    if ((m >= 1 and n == 0) and abs(dif) == 1) or ((n >= 1 and m == 0) and abs(dif) == 0):
       return 1
        
    if ((m >= 1 and n == 0) and abs(dif) != 1) or ((n >= 1 and m == 0) and abs(dif) != 0) or (m >= 1 and n >= 1):
        return 3
        
    if m == 0 and n == 0 and d > 0:
        return 2

    if (x+o == 9) or (x == 0 and o == 0 and d == 9):
        return 1
    

    

def main():
    for i in range(int(input().strip())):
        lst = []
        for i in range(3):
            lst.append(list(input().strip()))
        print('{0}'.format(ticTacToe(lst)))


if __name__ == "__main__":
    main()