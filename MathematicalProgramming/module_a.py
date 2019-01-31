def mAp1(A,c):
    neighbour_count = 0;
    cell_value = A[c[0]][c[1]];

    #Number of lists = number of rows
    if(c[0] != len(A) - 1):
        if(A[c[0] + 1][c[1]] == 1):
            neighbour_count += 1;

        if(c[1] != len(A[0]) - 1):
            if(A[c[0] + 1][c[1] + 1] == 1):
                neighbour_count += 1;


    #All the lists are the same width so
    #compare to the length of first list
    if(c[1] != len(A[0]) - 1):
        if(A[c[0]][c[1] + 1] == 1):
            neighbour_count += 1;

        if (c[0] != 0):
            if(A[c[0] - 1][c[1] + 1] == 1):
                neighbour_count += 1;

    if(c[0] != 0):
        if(A[c[0] - 1][c[1]] == 1):
            neighbour_count += 1;

        if(c[1] != 0):
            if(A[c[0] - 1][c[1] - 1] == 1):
                neighbour_count += 1;

    if(c[1] != 0):
        if(A[c[0]][c[1] - 1] == 1):
            neighbour_count += 1;

        if(c[0] != len(A) - 1):
            if(A[c[0] + 1][c[1] - 1] == 1):
                neighbour_count += 1;

    if(cell_value == 1):
        if(neighbour_count <= 1):
            return 0;
        if(neighbour_count >= 4):
            return 0;
        if(neighbour_count > 1 and neighbour_count < 4):
            return cell_value;
    else:
        if(neighbour_count == 3):
            return 1;

    return cell_value;

def mAp2(A):
    next_matrix = [];
    row_list = [];

    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            c = (i, j);

            row_list.append(mAp1(A, c));
        next_matrix.append(row_list);
        row_list = [];

    return next_matrix;

def mAp3(A, k):
    for i in range(0, k):
        A = mAp2(A);

    return A;

def mAp4(A, k):
    next_matrix = [];
    row_list = [];

    neighbours = [];
    last_neighbour_state = []
    last_cell_state = [];

    for num in range(0, k):
        for i in range(0, len(A)):
            for j in range(0, len(A[i])):
                c = (i, j);

                neighbours = check_neighbours(A, c);

                if(neighbours != last_neighbour_state and c != last_cell_state):
                    row_list.append(mAp1(A, c));

                last_neighbour_state = neighbours;
                last_cell_state = c;

            next_matrix.append(row_list);
            row_list = [];

    return next_matrix;

def check_neighbours(A, c):
    neighbour_list = [];

    if(c[0] != len(A) - 1):
        neighbour_list.append(A[c[0] + 1][c[1]]);

        if(c[1] != len(A[0]) - 1):
            neighbour_list.append(A[c[0] + 1][c[1] + 1]);

    if (c[1] != len(A[0]) - 1):
        neighbour_list.append(A[c[0]][c[1] + 1]);

        if(c[0] != 0):
            neighbour_list.append(A[c[0] - 1][c[1]] + 1);

    if(c[0] != 0):
        neighbour_list.append(A[c[0] - 1][c[1]]);

        if(c[1] != 0):
            neighbour_list.append(A[c[0] - 1][c[1] - 1]);

    if(c[1] != 0):
        neighbour_list.append(A[c[0]][c[1] - 1]);

        if(c[0] != len(A) - 1):
            neighbour_list.append((A[c[0] + 1][c[1] - 1]));

    return neighbour_list;

def mAp5():
    import random;
    state_count = 0;
    matrix_list = [];

    while (state_count <= 10):
        for i in range(1, 30):
            for j in range(1, 30):
                matrix = []
                row = [];

                for a in range(0, i + 1):
                    for b in range(0, j + 1):
                        row.append(random.randint(0, 1));

                    matrix.append((row));
                    row = [];

                if (matrix == mAp2(matrix) and matrix not in matrix_list):
                    state_count += 1;
                    matrix_list.append(matrix);
                    print('yes')
                    # print(state_count)

                matrix = [];

                if (state_count >= 10):
                    break;

    return matrix_list;

def mAp7(A, k):
    for i in range(0, k):
        A = torus_iteration(A);

    for i in A:
        print(i)
    #return A;

def torus_iteration(A):
    next_matrix = [];
    row_list = [];

    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            c = (i, j);

            row_list.append(torus(A, c));
        next_matrix.append(row_list);
        row_list = [];

    return next_matrix;

def torus(A, c):
    neighbour_count = 0;
    cell_value = A[c[0]][c[1]];

    # Number of lists = number of rows
    if(c[0] != len(A) - 1):
        if(A[c[0] + 1][c[1]] == 1):
            neighbour_count += 1;

        if(c[1] != len(A[0]) - 1):
            if(A[c[0] + 1][c[1] + 1] == 1):
                neighbour_count += 1;
    else:
        if(A[0][c[1]] == 1):
            neighbour_count += 1;

        if(c[1] != len(A[0]) - 1):
            if(A[0][c[1] + 1] == 1):
                neighbour_count += 1;

        if(c[1] != 0):
            if(A[0][c[1] - 1] == 1):
                neighbour_count += 1;

    # All the lists are the same width so
    # compare to the length of first list
    if(c[1] != len(A[0]) - 1):
        if(A[c[0]][c[1] + 1] == 1):
            neighbour_count += 1;

        if(c[0] != 0):
            if(A[c[0] - 1][c[1] + 1] == 1):
                neighbour_count += 1;
    else:
        if(A[c[0]][0] == 1):
            neighbour_count += 1;

        if(c[0] != len(A) - 1):
            if(A[c[0] + 1][0] == 1):
                neighbour_count += 1;

        if(c[0] != 0):
            if(A[c[0] - 1][0] == 1):
                neighbour_count += 1;

    if(c[0] != 0):
        if(A[c[0] - 1][c[1]] == 1):
            neighbour_count += 1;

        if(c[1] != 0):
            if(A[c[0] - 1][c[1] - 1] == 1):
                neighbour_count += 1;
    else:
        if(A[len(A) - 1][c[1]] == 1):
            neighbour_count += 1;

        if(c[1] != 0):
            if(A[len(A) - 1][c[1] - 1] == 1):
                neighbour_count += 1;

        if(c[1] != len(A[0]) - 1):
            if(A[len(A) - 1][c[1] + 1] == 1):
                neighbour_count += 1;


    if(c[1] != 0):
        if(A[c[0]][c[1] - 1] == 1):
            neighbour_count += 1;

        if(c[0] != len(A) - 1):
            if(A[c[0] + 1][c[1] - 1] == 1):
                neighbour_count += 1;
    else:
        if(A[c[0]][len(A[0]) - 1] == 1):
            neighbour_count += 1;

        if(c[0] != len(A) - 1):
            if(A[c[0] + 1][len(A[0]) - 1] == 1):
                neighbour_count += 1;

        if(c[0] != 0):
            if(A[c[0] - 1][len(A[0]) - 1] == 1):
                neighbour_count += 1;

    '''
    if(c[0] == 0):

    if(c[0] == len(A) - 1):

    if(c[1] == 0):

    if(c[1] == len(A[0]) - 1)
    '''

    if(cell_value == 1):
        if(neighbour_count <= 1):
            return 0;
        if(neighbour_count >= 4):
            return 0;
        if(neighbour_count > 1 and neighbour_count < 4):
            return cell_value;
    else:
        if(neighbour_count == 3):
            return 1;

    return cell_value;


def main():

#    print('''mAp1([[1,0,1,0],
#      [0,0,1,0],
#      [0,0,0,0],
#      [1,0,1,1]], (1, 1)): ''' + str(mAp1([[1,0,1,0],
#                                           [0,0,1,0],
#                                           [0,0,0,0],
#                                           [1,0,1,1]], (3, 1))));
#    print();
#    print('''mAp2([[1,0,1,0],
#      [0,0,1,0],
#      [0,0,0,0],
#      [1,0,1,1]]): ''' + str(mAp2([[1,0,1,0],
#                                   [0,0,1,0],
#                                   [0,0,0,0],
#                                   [1,0,1,1]])));
#    print();
#    print('''mAp3([[1,0,1,0],
#      [0,0,1,0],
#      [0,0,0,0],
#      [1,0,1,1]], 3): ''' + str(mAp3( [[1,0,1,0],
#                                       [0,0,1,0],
#                                       [0,0,0,0],
#                                       [1,0,1,1]], 3)));
#    print();
#    print('''mAp4([[1,0,1,0],
#     [0,0,1,0],
#      [0,0,0,0],
#      [1,0,1,1]], 1000000): ''' + str(mAp4([[1, 0, 1, 0],
#                                            [0, 0, 1, 0],
#                                            [0, 0, 0, 0],
#                                            [1, 0, 1, 1]], 1000000)));

#    print('mAp5(): ' + str(mAp5()));

    print(mAp7( [[0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,1,1,1],
                 [0,0,1,0,1],
                 [0,0,1,1,1]], 1));

    ''' Expected
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    '''


if __name__ == '__main__':
    main();