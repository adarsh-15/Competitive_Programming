def let_combo(lst, n, i, osf, ans):
    if i == len(lst):
        ans.append(osf)
        return

    for j in range(len(lst[i])):
        temp = lst[i][j]
        let_combo(lst, n, i + 1, osf + temp, ans)
        temp = ""

    return ans


def main():
    str_com = input().strip()
    lst = list(str_com)
    fin_lst = []
    map_lst = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
               ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    for i in lst:
        fin_lst.append(map_lst[int(i)])

    ans = let_combo(fin_lst, len(fin_lst), 0, "", [])
    print(ans)


if __name__ == "__main__":
    main()
