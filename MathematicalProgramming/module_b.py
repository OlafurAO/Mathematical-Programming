def mBp3(perm):
    young_table = [[]] * int(len(perm)/2);

    for i in range(len(young_table)):
        young_table[i] = [0] * int(len(perm)/2)

    #young_table[0][0] = min(perm);

    count = 0;

    for p in perm:
        found_place = False;
        for i in range(len(young_table)):
            for j in range(len(young_table)):
                if(count == 0):
                    young_table[i][j] = p;
                    found_place = True;
                    count += 1;
                    break;

                if(young_table[i][j] == 0):
                    young_table = find_place(young_table, p, (i, j));
                    found_place = True;
                    count += 1;
                    break;

            if(found_place):
                break;

    for i in range(len(young_table)):
        young_table[i] = [value for value in young_table[i] if value != 0];

    return young_table;

def find_place(young_table, p, pos):
    #young_table[pos[0]][pos[1]] = p;

    for i in range(pos[1] - 1, -1, -1):
        if(young_table[0][i] <= p):
            young_table[0][i + 1] = p;
            break;

        elif(young_table[0][i] > p):
            '''
            for k in range(len(young_table) - 1, 0, -1):
                young_table[k][i] = young_table[k - 1][0];
            young_table[0][i] = p;
            '''

            if(i == 0):
                for k in range(len(young_table) - 1, 0, -1):
                    young_table[k][0] = young_table[k - 1][0];

                young_table[0][i] = p;

            else:
                if(young_table[len(young_table) - 1][0] != 0):
                    for k in range(len(young_table) - 1, 0, -1):
                        young_table[k][i] = young_table[k - 1][i];
                    young_table[0][i] = p;


    return young_table;

def main():
    print(mBp3([3,5,2,1,4,6]))


if __name__ == '__main__':
    main();