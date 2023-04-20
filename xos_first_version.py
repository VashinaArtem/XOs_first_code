def check_for_win(xos):
    if (xos[0][0] == xos[0][1] == xos[0][2] == 'x') or (xos[0][0] == xos[0][1] == xos[0][2] == 'o'):
        print(f' победа {xos[0][0]}')
        return True
    elif (xos[1][0] == xos[1][1] == xos[1][2] == 'x') or (xos[1][0] == xos[1][1] == xos[1][2] == 'o'):
        print(f' победа {xos[1][0]}')
        return True
    elif (xos[2][0] == xos[2][1] == xos[2][2] == 'x') or (xos[1][0] == xos[1][1] == xos[1][2] == 'o'):
        print(f' победа {xos[2][0]}')
        return True

    if (xos[0][0] == xos[1][0] == xos[2][0] == 'x') or (xos[0][0] == xos[1][0] == xos[2][0] == 'o'):
        print(f' победа {xos[0][0]}')
        return True
    elif (xos[0][1] == xos[1][1] == xos[2][1] == 'x') or (xos[0][1] == xos[1][1] == xos[2][1] == 'o'):
        print(f' победа {xos[1][0]}')
        return True
    elif (xos[0][2] == xos[1][2] == xos[2][2] == 'x') or (xos[0][2] == xos[1][2] == xos[2][2] == 'o'):
        print(f' победа {xos[2][0]}')
        return True

    elif (xos[0][0] == xos[1][1] == xos[2][2] == 'x') or (xos[1][0] == xos[1][1] == xos[1][2] == 'o'):
        print(f' победа {xos[0][0]}')
        return True
    elif (xos[0][2] == xos[1][1] == xos[2][0] == 'x') or (xos[1][0] == xos[1][1] == xos[1][2] == 'o'):
        print(f' победа {xos[0][0]}')
        return True

def upload_matrix(xos_add):

    for k in range(0, 8):
        row = int(input("enter row: "))
        column = int(input("enter column: "))
        choice = input("enter your choice (x or o): ")
        if choice == 'x' or choice == 'o':
            continue
        else:
            choice

        xos_add[row][column] = choice

        for i in range(len(xos_add)):
            for j in range(len(xos_add[i])):
                print(xos_add[i][j] + " ", end=' ')
            print()

        if check_for_win(xos_add):
            break

xos = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

upload_matrix(xos)